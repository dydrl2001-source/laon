# 메인작업 — Governance Hub

D 드라이브 14+개 자동화 프로젝트의 정책·스킬·에이전트·플레이북을 단일 진실의 원천(SSOT)으로 관리하는 저장소.

> **이 저장소가 GitHub repo가 되는 이유**: 도메인 노하우 영구 보존 + 새 PC에서 git clone 1회로 동일 환경 복원 + 5년 후 인수인계 자료.

## 정책 (자동 상속)

@policies/알렉스-7원칙.md
@policies/케어포-도메인.md
@policies/비밀처리.md
@policies/백업.md
@policies/문서화.md
@policies/mcp-구성.md
@policies/슬래시-커맨드.md
@policies/에이전트-병렬.md

위 import 디렉티브로 분야별 정책이 자동 로드됩니다. 각 정책은 단일 책임을 가집니다.
**알렉스-7원칙은 모든 정책 중 최상위 — SSoT·SoC·Consistency·Atomicity·Idempotency·No Silent Fallback·Doc-first 7가지가 다른 정책 해석의 기반이 됩니다.**

## 폴더 구조

| 폴더/파일 | 역할 | 상태 |
|---|---|:---:|
| `사용매뉴얼.md` | 종합 사용 가이드 (이 문서부터 보세요) | ✅ |
| `policies/` (7종) | 도메인·운영·보안 정책 | ✅ Phase 1 |
| `manifest.yaml` | 15개 프로젝트 정본 인덱스 (SSOT) | ✅ Phase 2 |
| `tools/` | 거버넌스 운영 스크립트 (sync_review_targets) | ✅ Phase 2.5 |
| `hooks/` | 하네스 훅 PowerShell 스크립트 (settings.json이 호출) | ✅ Tier 1 |
| `skills/` (4종) | 재사용 자동화 패턴 | ✅ Phase 3 |
| `agents/` (3종) | 도메인 전문 에이전트 정의 | ✅ Phase 4 |
| `playbooks/` (5종) | 표준 운영 절차 | ✅ Phase 5 |
| `templates/` | 새 프로젝트 스타터 | ✅ Phase 6 |

## manifest.yaml 사용

본 파일이 자동화 인벤토리의 **SSOT**. `~/.claude/review_targets.json`은 derivative.

신규 프로젝트 합류 시:
1. `manifest.yaml` `projects:` 항목 추가
2. 필요 시 `backup.zip_targets` 또는 `mirror_targets`에 경로 추가
3. `D:\백업도구\backup_projects.ps1` `$zipFolders`/`$mirrorFolders` 동기화
4. `~/.claude/review_targets.json` 동기화 (Phase 2.5에서 자동화 예정)
5. git commit + push

## 글로벌 적용

`~/.claude/CLAUDE.md`에 다음 한 줄 추가하면 모든 Claude Code 세션에 정책 자동 상속:

```
@D:\메인작업\CLAUDE.md
```

## ⛔ 대전제 — 메인작업 세션은 다른 프로젝트에 코드 안 친다

**이것은 협상 불가의 1차 대전제다.** 알렉스-7원칙(SoC/SRP)의 거버넌스 레벨 적용. 매니저는 **읽기 전용 거버넌스 레이어**이며, 다른 프로젝트의 코드·설정·자동화에 손대지 않는다.

이중 안전장치:
- **시스템 차단**: `hooks/block_off_project_writes.ps1` 가 PreToolUse 단계에서 다른 D 프로젝트 폴더 쓰기 시도를 자동 거부 (manifest.yaml 등록 전체 대칭 격리)
- **정책 명시**: 본 섹션이 사람·AI 모두에게 의도를 선언

### 절대 하지 않는 것 (대전제의 구체화)

1. **다른 프로젝트 폴더의 코드·설정 파일 수정** (D:\carefor_*, D:\블로그자동화, D:\주식 등)
2. 기존 `.env` 통합·이동·심볼릭링크
3. 기존 Task Scheduler 등록물 변경 / sys.path·PYTHONPATH 조작

### 다른 프로젝트 통합이 필요할 때

해당 프로젝트 폴더로 가서 별도 Claude Code 세션을 켠다. 그 세션에서:
- `D:\메인작업\tools\` 의 공통 도구를 import / CLI 호출
- `D:\메인작업\playbooks\` 의 통합 절차를 따라 작업
- 메인작업의 정책·에이전트 카드는 그대로 자동 상속됨 (글로벌 import 체인)

이 분담 구조가 알렉스 7원칙 중 #2(SoC/SRP)와 #6(No Silent Fallback)을 거버넌스 레벨에서 보장한다.

## 변경 이력

- 2026-05-08: Phase 0 git init + Phase 1 정책 7종 마이그레이션 (~/.claude/CLAUDE.md에서 분할)
- 2026-05-08: .gitignore에 `.claude/settings.local.json` 추가 (로컬 전용 추적 제외)
- 2026-05-08: Phase 2 — manifest.yaml 작성 (15개 프로젝트 정본 인벤토리 + 백업·슬래시커맨드 매핑 통합)
- 2026-05-08: Phase 2.5 — `tools/sync_review_targets.py` (manifest → review_targets path 동기화)
- 2026-05-08: Phase 3 — skills 4종 (한글 파일명 / NotebookLM 라우팅 / 디스크 사고 회피 / 다관점 회의)
- 2026-05-08: Phase 4 — agents 3종 (케어포 도메인 / 평가매뉴얼 자문 / 백업 무결성 검사)
- 2026-05-08: Phase 5 — playbooks 4종 추가 (매월 백업 / 신규 온보딩 / GitHub 동기화 / C 디스크 해소)
- 2026-05-08: Phase 6 — templates/automation-skeleton (CLAUDE.md / README.md / .gitignore / .env.example)
- 2026-05-08: 사용매뉴얼.md 종합 작성 — 12장 구성, 일상 사용·트러블슈팅·새 PC 복원 단일 가이드
- 2026-05-08: Task Scheduler `프로젝트백업_매월1일` 등록 완료 (NextRunTime 2026-06-01 09:00)
- 2026-05-08: Anthropic 엔지니어급 메타 에이전트 5종 추가 (Staff SWE / SRE / Security / Applied AI / Perf·Cost) — `agents/` 도메인 3 + 엔지니어급 5 = 8종 풀, `policies/에이전트-병렬.md` 작업별 조합 매핑 반영
- 2026-05-09: 하네스 엔지니어링 Tier 1 — `hooks/` 폴더 신설 (`block_off_project_writes.ps1` / `statusline.ps1`). `~/.claude/settings.json`에 PreToolUse 차단 훅 + 읽기전용 명령 12종 allowlist + statusLine 등록. 거버넌스 3대 금지선 #1이 자연어 약속에서 시스템 차단으로 격상.
- 2026-05-11: Tier 2 — `/백업확인` 슬래시커맨드 (`~/.claude/commands/백업확인.md`). SRE + 백업무결성 에이전트 병렬 호출로 매월 2일 한 줄 검증. `policies/슬래시-커맨드.md` 카탈로그 + 사용매뉴얼 11장 동기화.
- 2026-05-11: Tier 2 옵션 B — statusline 매월 백업검증 리마인더. `D:\백업도구\결과\<YYYY-MM>_verified.txt` sentinel 미존재 시 "!백업검증 필요(/백업확인)" 표시. `/백업확인`이 OK/WARNING 판정 시 sentinel 생성 → 알림 자동 소거. 3개 시나리오 pipe-test 통과.
- 2026-05-13: 신규 프로젝트 `D:\주식` 거버넌스 합류 — 키움 REST API 기반 개인용 주식 분석 비서. `manifest.yaml` projects 16번째 항목 추가 + `backup.zip_targets`에 `D:\주식` 추가 + `updated` 갱신. `tools/sync_review_targets.py` 실행으로 `~/.claude/review_targets.json` 자동 동기화 (주식 포함). PreToolUse 차단 훅이 의도대로 작동해 D:\주식 내부 수정은 별도 세션에서 진행하도록 분담.
- 2026-05-13: `hooks/block_off_project_writes.ps1` **대칭 격리**로 확장 — 메인작업 단방향 → N-방향. `manifest.yaml` projects[*].path 파싱해 등록 프로젝트면 모두 "내 경로만 허용" 규칙 적용. D:\주식·블로그·carefor 등 모든 프로젝트가 양방향 보호받음. 신규 프로젝트는 manifest 등록만으로 자동 보호 편입. pipe-test 7/7 통과. settings.json 변경 없음 (훅 스크립트 자체만 갱신).
- 2026-05-19: Google Cloud AI Agent Trends 2026 보고서 트렌드 1·2 적용 — 글로벌 슬래시커맨드 `/매일아침` 신설 (`~/.claude/commands/매일아침.md`). 케어포-도메인 + 평가매뉴얼-자문 + 엔지니어-SRE + 운영 마감 룰 4명 병렬 → 한 페이지 인사이트 + Gmail 초안 자동 작성. 원장님 역할이 "운영자 → 에이전트 감독자"로 전환되는 첫 단계. `policies/슬래시-커맨드.md` 카탈로그 동기화.
- 2026-05-19: `/매일아침` 메일 수신 주소 변경 — pkw4260@gmail.com → **pkw426@naver.com** (원장님 일상 확인용 주메일이 네이버). 발신은 Gmail MCP 그대로, 수신만 네이버로 전달.
- 2026-05-19: 공통 알림 인프라 신설 — `tools/notify.py` (Windows 토스트 헬퍼, Python import + CLI 둘 다) + `playbooks/프로젝트별-알림-통합.md` (적용 절차 + 우선순위 7단계). 주식 프로젝트의 `_send_toast_notification` 패턴을 거버넌스 자산으로 일반화. 각 프로젝트 통합(carefor·백업도구·블로그자동화 등)은 차단 훅 때문에 해당 프로젝트 세션에서 분담.
- 2026-05-21: **알렉스 7원칙 거버넌스 의무화** — aldegad/alex-core-invariants 의 7원칙(SSoT·SoC·Consistency·Atomicity·Idempotency·No Silent Fallback·Doc-first/Plan-first)을 `policies/알렉스-7원칙.md` 로 박고 정책 import 체인 **최상단**에 배치 → 모든 자동화 프로젝트 자동 상속. 박광우님 자동화 보강 갭(Atomicity 블로그·케어포작성 / Idempotency 카톡보고·희망이음반자동 / Doc-first 새 영역) 우선순위 명시. 동시에 "코드 비침습 3대 금지선"을 **"대전제 — 메인작업 세션은 다른 프로젝트에 코드 안 친다"** 로 격상 (시스템 차단 훅 + 정책 명시 이중 안전장치).
