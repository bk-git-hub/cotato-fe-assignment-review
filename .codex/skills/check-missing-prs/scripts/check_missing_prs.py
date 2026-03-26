#!/usr/bin/env python3
import argparse
import json
import re
import subprocess
import sys
from pathlib import Path
from typing import Any, Dict, List, Optional, Set


DEFAULT_REPO = "IT-Cotato/13th-Frontend-Assignment"
AUTO_EXCLUDED_BASE_BRANCHES = {"main", "master", "develop", "dev"}
WEEK_BRANCH_RE = re.compile(r"^(?P<handle>.+)-week-?0*(?P<week>\d+)$", re.IGNORECASE)


def run_gh(args: List[str]) -> str:
    result = subprocess.run(
        ["gh", *args],
        check=True,
        capture_output=True,
        text=True,
    )
    return result.stdout


def parse_week_token(raw: Optional[str]) -> Optional[int]:
    if raw is None:
        return None
    match = re.search(r"week-?0*(\d+)|^0*(\d+)$", raw, re.IGNORECASE)
    if not match:
        raise ValueError(f"Could not parse week number from '{raw}'.")
    group = match.group(1) or match.group(2)
    return int(group)


def normalize_handle(value: str) -> str:
    return value.strip().lower()


def infer_week_from_workspace(cwd: Path) -> Optional[int]:
    objectives_dir = cwd / "weekly-objectives"
    if not objectives_dir.exists():
        return None

    weeks: List[int] = []
    for path in objectives_dir.glob("week-*.md"):
        match = re.search(r"week-0*(\d+)\.md$", path.name, re.IGNORECASE)
        if match:
            weeks.append(int(match.group(1)))
    return max(weeks) if weeks else None


def fetch_branches(repo: str) -> List[str]:
    output = run_gh(
        ["api", f"repos/{repo}/branches", "--paginate", "--jq", ".[].name"]
    )
    return [line.strip() for line in output.splitlines() if line.strip()]


def fetch_prs(repo: str) -> List[Dict[str, Any]]:
    output = run_gh(
        [
            "pr",
            "list",
            "--repo",
            repo,
            "--state",
            "all",
            "--limit",
            "200",
            "--json",
            "number,title,state,baseRefName,headRefName,url",
        ]
    )
    return json.loads(output)


def infer_week_from_repo(branches: List[str], prs: List[Dict[str, Any]]) -> Optional[int]:
    weeks: Set[int] = set()

    for branch in branches:
        match = WEEK_BRANCH_RE.match(branch)
        if match:
            weeks.add(int(match.group("week")))

    for pr in prs:
        match = WEEK_BRANCH_RE.match(pr["headRefName"])
        if match:
            weeks.add(int(match.group("week")))

    return max(weeks) if weeks else None


def build_roster(branches: List[str], excluded_handles: Set[str]) -> List[str]:
    roster: List[str] = []
    for branch in branches:
        normalized = normalize_handle(branch)
        if normalized in AUTO_EXCLUDED_BASE_BRANCHES:
            continue
        if normalized in excluded_handles:
            continue
        if WEEK_BRANCH_RE.match(branch):
            continue
        roster.append(branch)
    return sorted(roster, key=str.lower)


def week_branch_lookup(branches: List[str], week: int) -> Dict[str, List[str]]:
    lookup: Dict[str, List[str]] = {}
    for branch in branches:
        match = WEEK_BRANCH_RE.match(branch)
        if not match:
            continue
        if int(match.group("week")) != week:
            continue
        handle = normalize_handle(match.group("handle"))
        lookup.setdefault(handle, []).append(branch)
    return lookup


def matching_prs_for_handle(
    prs: List[Dict[str, Any]], handle: str, week: int
) -> List[Dict[str, Any]]:
    normalized_handle = normalize_handle(handle)
    matches: List[Dict[str, Any]] = []
    for pr in prs:
        week_match = WEEK_BRANCH_RE.match(pr["headRefName"])
        if not week_match or int(week_match.group("week")) != week:
            continue
        head_handle = normalize_handle(week_match.group("handle"))
        base_handle = normalize_handle(pr["baseRefName"])
        if head_handle == normalized_handle or base_handle == normalized_handle:
            matches.append(pr)
    return sorted(matches, key=lambda item: item["number"])


def summarize(
    repo: str,
    week: int,
    roster: List[str],
    branches: List[str],
    prs: List[Dict[str, Any]],
) -> Dict[str, Any]:
    branch_lookup = week_branch_lookup(branches, week)

    submitted: List[Dict[str, Any]] = []
    closed_without_merge: List[Dict[str, Any]] = []
    branch_only: List[Dict[str, Any]] = []
    missing: List[Dict[str, Any]] = []

    for handle in roster:
        matches = matching_prs_for_handle(prs, handle, week)
        open_or_merged = [pr for pr in matches if pr["state"] in {"OPEN", "MERGED"}]
        closed_only = [pr for pr in matches if pr["state"] == "CLOSED"]
        week_branches = branch_lookup.get(normalize_handle(handle), [])

        if open_or_merged:
            submitted.append({"handle": handle, "prs": open_or_merged})
        elif closed_only:
            closed_without_merge.append({"handle": handle, "prs": closed_only})
        elif week_branches:
            branch_only.append({"handle": handle, "branches": week_branches})
        else:
            missing.append({"handle": handle})

    return {
        "repo": repo,
        "week": week,
        "roster_size": len(roster),
        "submitted": submitted,
        "closed_without_merge": closed_without_merge,
        "branch_only": branch_only,
        "missing": missing,
    }


def print_text(summary: Dict[str, Any]) -> None:
    print(f"Repo: {summary['repo']}")
    print(f"Week: {summary['week']}")
    print(f"Roster size: {summary['roster_size']}")
    print()

    def print_section(title: str, rows: List[Dict[str, Any]], formatter) -> None:
        print(f"{title} ({len(rows)}):")
        if not rows:
            print("- none")
            print()
            return
        for row in rows:
            print(f"- {formatter(row)}")
        print()

    print_section(
        "Submitted",
        summary["submitted"],
        lambda row: f"{row['handle']}: "
        + ", ".join(
            f"PR #{pr['number']} [{pr['state']}] {pr['headRefName']}"
            for pr in row["prs"]
        ),
    )
    print_section(
        "Closed without merge",
        summary["closed_without_merge"],
        lambda row: f"{row['handle']}: "
        + ", ".join(
            f"PR #{pr['number']} [{pr['state']}] {pr['headRefName']}"
            for pr in row["prs"]
        ),
    )
    print_section(
        "Branch exists but no PR",
        summary["branch_only"],
        lambda row: f"{row['handle']}: {', '.join(row['branches'])}",
    )
    print_section(
        "Missing branch and PR",
        summary["missing"],
        lambda row: row["handle"],
    )


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Check which student handles have not submitted a weekly PR."
    )
    parser.add_argument("week", nargs="?", help="Week number such as 2, week2, or week-2.")
    parser.add_argument(
        "--repo",
        default=DEFAULT_REPO,
        help=f"GitHub repository in owner/name form. Default: {DEFAULT_REPO}",
    )
    parser.add_argument(
        "--exclude",
        default="",
        help="Comma-separated base branches to exclude from the inferred roster.",
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="Emit JSON instead of human-readable text.",
    )
    args = parser.parse_args()

    try:
        week = parse_week_token(args.week)
    except ValueError as exc:
        print(str(exc), file=sys.stderr)
        return 2

    excluded_handles = {
        normalize_handle(item)
        for item in args.exclude.split(",")
        if item.strip()
    }

    try:
        branches = fetch_branches(args.repo)
        prs = fetch_prs(args.repo)
    except subprocess.CalledProcessError as exc:
        sys.stderr.write(exc.stderr or str(exc))
        return exc.returncode or 1

    if week is None:
        week = infer_week_from_workspace(Path.cwd()) or infer_week_from_repo(branches, prs)

    if week is None:
        print(
            "Could not infer the target week. Pass a week like '2' or 'week2'.",
            file=sys.stderr,
        )
        return 2

    roster = build_roster(branches, excluded_handles)
    summary = summarize(args.repo, week, roster, branches, prs)

    if args.json:
        print(json.dumps(summary, ensure_ascii=False, indent=2))
    else:
        print_text(summary)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
