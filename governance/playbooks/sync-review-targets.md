# 플레이북: manifest → review_targets 동기화

## 언제 실행하는가

`D:\메인작업\manifest.yaml`의 `projects` 항목에서 **path가 변경됐을 때**:
- 새 프로젝트를 manifest에 추가한 직후
- 기존 프로젝트 폴더를 다른 드라이브/위치로 이동한 후
- D 드라이브 이전 같은 대규모 경로 변경 후

## 무엇이 동기화되나

- `manifest.yaml` → `~/.claude/review_targets.json`
- **path 필드만** 동기화 (양쪽 모두 있는 프로젝트 한정)
- review_targets.json 의 agents·domain_agents·extensions·readonly·notebooklm_required 등 기존 메타는 보존

## 절차

### 1. dry-run으로 변경 사항 미리 확인

```powershell
python D:\메인작업\tools\sync_review_targets.py --dry-run
```

출력 예:
```
변경 사항:
  - 운영위원회 작성: C:/Users/user/운영위원회 작성 -> D:/운영위원회 작성
  ...
--dry-run 모드 — 파일 미변경.
```

### 2. 실제 적용

```powershell
python D:\메인작업\tools\sync_review_targets.py
```

자동 백업: `~/.claude/review_targets.json.backup-YYYYMMDD-HHMMSS`

### 3. 검증

```powershell
git -C "D:\메인작업" diff --stat
type "$env:USERPROFILE\.claude\review_targets.json"
```

## 트러블슈팅

| 에러 | 원인 | 해결 |
|---|---|---|
| `ModuleNotFoundError: yaml` | pyyaml 미설치 | `pip install pyyaml` |
| `manifest 파일 없음` | 경로 변경됨 | tools/sync_review_targets.py 의 `MANIFEST` 상수 갱신 |
| `manifest 미등록 review-only` 경고 | review_targets에만 있는 프로젝트 | manifest에 추가하거나 review_targets에서 정리 |

## 향후 자동화 검토

git pre-commit hook으로 `manifest.yaml` 변경 시 자동 sync 검토 가능 (Phase 7 후보).
