# tools/ — 거버넌스 운영 스크립트

매니저가 직접 실행하는 작은 유틸리티 스크립트 모음. **다른 프로젝트 코드를 건드리지 않고**, 매니저 메타데이터(manifest, ~/.claude/* 등)만 다루는 도구만 둠.

## 도구 목록

| 파일 | 용도 | 관련 플레이북 |
|---|---|---|
| `sync_review_targets.py` | manifest.yaml → ~/.claude/review_targets.json path 동기화 | `playbooks/sync-review-targets.md` |
| `notify.py` | 공통 Windows 토스트 알림 (산출물 완료 시) — Python import 또는 CLI 둘 다 가능 | `playbooks/프로젝트별-알림-통합.md` |

## 추가 원칙

- 외부 프로젝트 폴더의 코드/.env/config 절대 수정 금지 (코드 비침습 원칙)
- 모든 도구는 `--dry-run` 모드 지원 권장
- 파괴적 작업 전 자동 백업 (백업 파일명에 timestamp)
- 한 도구 = 한 책임

## 변경 이력

- 2026-05-08: Phase 2.5 — `sync_review_targets.py` 추가
- 2026-05-19: `notify.py` 추가 — 공통 Windows 토스트 알림 도구. 모든 자동화 프로젝트가 산출물 생성 직후 한 줄(Python `send_toast()` 또는 CLI `python notify.py --title ...`)로 박광우님 화면에 알림 띄울 수 있게 통합. 주식 프로젝트(cli/daily.py)의 `_send_toast_notification` 패턴을 일반화. winotify 미설치 시 조용히 스킵 — 호출 프로젝트의 작업 흐름 절대 안 막음.
