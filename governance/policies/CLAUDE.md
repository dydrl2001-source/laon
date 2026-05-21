# policies/ — 거버넌스 정책 모음

매니저가 모든 자동화 프로젝트에 자동 상속시키는 도메인·운영·보안 규칙.

## 정책 8종

| 파일 | 단일 책임 |
|---|---|
| `알렉스-7원칙.md` | **(Required, 모든 프로젝트 의무, 최상위)** SSoT / SoC·SRP / Consistency / Atomicity / Idempotency / No Silent Fallback / Doc-first·Plan-first |
| `케어포-도메인.md` | NotebookLM 우선 + 평가매뉴얼 + 점검 5가지 검증 + 야간점검 기준 |
| `비밀처리.md` | .env 분산 유지 / 통합 금지 / .gitignore 패턴 |
| `백업.md` | 매월 1일 09:00 / D:\에만 / 영상편집 미러링 / 디스크 압박 회피 |
| `문서화.md` | CLAUDE.md 150줄·즉시갱신·분할정책 / 버그 메모리화 |
| `mcp-구성.md` | 글로벌 MCP 5개 / Desktop 확장 임포트 / claude.ai 커넥터 |
| `슬래시-커맨드.md` | /점검 /운영위원회 /review /cross-review /full-review /백업확인 /매일아침 |
| `에이전트-병렬.md` | 13명 동시 투입 / Opus 4.7 활용 7원칙 |

## 정책 추가 / 변경 절차

1. 새 파일 생성 시 단일 책임 원칙 (한 정책 = 한 도메인)
2. 부모 `D:\메인작업\CLAUDE.md`의 `@policies/<이름>.md` import 라인 추가
3. 중복 검토 (다른 정책과 겹치면 통합 또는 분리)
4. git commit 메시지에 변경 의도 명시

## 변경 이력

- 2026-05-08: 초기 7종 마이그레이션 (`~/.claude/CLAUDE.md`에서 분할)
- 2026-05-21: 8번째 정책 `알렉스-7원칙.md` 신설 — aldegad/alex-core-invariants 의 7가지 구조적 불변원칙을 거버넌스 차원으로 의무화. import 체인 최상단 배치로 모든 자동화 프로젝트에 자동 상속. 박광우님 보강 필요 영역(Atomicity·Idempotency·Doc-first) 우선순위 명시.
