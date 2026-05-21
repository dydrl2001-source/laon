"""manifest.yaml → ~/.claude/review_targets.json 동기화.

manifest.yaml 의 projects 항목 중 `path` 만 review_targets.json 으로 반영.
review_targets.json 에 없는 추가 메타데이터(agents, domain_agents 등)는 보존.
실행 전 자동 백업.

사용:
    python D:/메인작업/tools/sync_review_targets.py [--dry-run]
"""
from __future__ import annotations

import argparse
import json
import os
import shutil
import sys
from datetime import datetime
from pathlib import Path

import yaml

MANIFEST = Path(r"D:\메인작업\manifest.yaml")
REVIEW_TARGETS = Path(os.path.expanduser(r"~\.claude\review_targets.json"))


def load_manifest() -> dict:
    return yaml.safe_load(MANIFEST.read_text(encoding="utf-8"))


def load_review() -> dict:
    return json.loads(REVIEW_TARGETS.read_text(encoding="utf-8"))


def backup(target: Path) -> Path:
    ts = datetime.now().strftime("%Y%m%d-%H%M%S")
    bk = target.with_suffix(f".json.backup-{ts}")
    shutil.copy2(target, bk)
    return bk


def sync(dry_run: bool = False) -> None:
    manifest = load_manifest()
    review = load_review()

    manifest_by_name = {p["name"]: p for p in manifest["projects"]}

    changes: list[str] = []
    for name, entry in review["projects"].items():
        if name not in manifest_by_name:
            changes.append(f"- (manifest 미등록) review-only: {name}")
            continue
        manifest_path = manifest_by_name[name]["path"].replace("\\", "/")
        if entry.get("path") != manifest_path:
            changes.append(
                f"- {name}: {entry.get('path')} -> {manifest_path}"
            )
            entry["path"] = manifest_path

    only_in_manifest = set(manifest_by_name) - set(review["projects"])
    if only_in_manifest:
        changes.append(
            "manifest 에는 있으나 review_targets 미등록 ("
            f"수동 추가 검토): {sorted(only_in_manifest)}"
        )

    if not changes:
        print("이미 동기화 상태 — 변경 없음.")
        return

    print("변경 사항:")
    for c in changes:
        print(f"  {c}")

    if dry_run:
        print("\n--dry-run 모드 — 파일 미변경.")
        return

    bk = backup(REVIEW_TARGETS)
    print(f"\n백업: {bk}")

    review["_updated"] = datetime.now().strftime("%Y-%m-%d")
    REVIEW_TARGETS.write_text(
        json.dumps(review, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    print(f"갱신 완료: {REVIEW_TARGETS}")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dry-run", action="store_true", help="변경 사항만 출력")
    args = parser.parse_args()

    if not MANIFEST.exists():
        sys.exit(f"manifest 파일 없음: {MANIFEST}")
    if not REVIEW_TARGETS.exists():
        sys.exit(f"review_targets 파일 없음: {REVIEW_TARGETS}")

    sync(dry_run=args.dry_run)


if __name__ == "__main__":
    main()
