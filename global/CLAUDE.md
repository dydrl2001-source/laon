# 푸른초장요양원2 — 글로벌

## 기관 기본 정보

| 항목 | 내용 |
|------|------|
| 기관명 | 푸른초장요양원2 |
| 기관기호 | 14725000180 |
| 케어포 아이디 | 박광우 |
| 케어포 주소 | https://www.carefor.co.kr |
| 블로그 | https://blog.naver.com/puren5704 |
| GitHub 거버넌스 | https://github.com/pkw4260-coder/automation-governance |

※ 로그인 비밀번호는 보안상 별도 `.env` 파일로 관리

## 거버넌스 허브 자동 상속

@D:\메인작업\CLAUDE.md

위 한 줄로 D:\메인작업의 마스터 CLAUDE.md가 import되고, 그 안의 `@policies/*.md` 7종도 자동 로드됩니다 (정책: 케어포-도메인 / 비밀처리 / 백업 / 문서화 / mcp-구성 / 슬래시-커맨드 / 에이전트-병렬).

## 설치된 플러그인 마켓플레이스 (참조용)

| 마켓플레이스 | 주요 내용 |
|---|---|
| anthropic-agent-skills | Anthropic 공식 스킬 (pptx, pdf, xlsx 등) |
| claude-plugins-official | Anthropic 공식 플러그인 33개 |
| gptaku_plugins | insane-search, deep-research, nopal 등 11개 |
| claude-skills | 235개 스킬 (마케팅·엔지니어링·컴플라이언스 등 9개 도메인) |
| awesome-claude-code-toolkit | 135 에이전트 + 35 스킬 + 훅/템플릿 |
| claude-code-plugins-plus-skills | 340 플러그인 + 1367 스킬 (CCPI 패키지 매니저) |

터미널 재시작 시 자동 로드됨.

## D 드라이브 자동화 프로젝트 위치 (2026-05-08)

C:\ 디스크 압박 해소 위해 모든 자동화 프로젝트를 D:\ 루트로 이전. 상세 경로 표는 거버넌스 repo의 `manifest.yaml`(Phase 2 예정)에서 관리.

`~/.claude/review_targets.json`은 D 경로로 갱신 완료. 신규 프로젝트 추가 시 한 줄 추가.

## 변경 이력

- 2026-05-08: D 드라이브 거버넌스 허브로 정책 분리. 본 글로벌 파일은 기관정보 + import 라인 + 마켓플레이스 참조만 유지. 분할 전 백업: `~/.claude/CLAUDE.md.backup-20260508-151010`
- 2026-05-09: 하네스 엔지니어링 Tier 1 적용 — `~/.claude/settings.json`에 ① PreToolUse 차단 훅 (`D:\메인작업\hooks\block_off_project_writes.ps1` — 거버넌스 세션에서 다른 D 프로젝트 수정 시도 차단) ② 읽기전용 PowerShell·git 명령 12종 allowlist ③ statusLine (`D:\메인작업\hooks\statusline.ps1` — 폴더 + D 드라이브 여유 + 1관/2관 경고). 훅 인식 위해 `/hooks` 메뉴 1회 또는 세션 재시작 필요.
- 2026-05-11: 글로벌 슬래시커맨드 `/백업확인` 신설 (`~/.claude/commands/백업확인.md`). 매월 2일 한 줄 호출 → SRE + 백업무결성 에이전트 병렬 검증.
- 2026-05-11: statusline 자동 리마인더 추가. `D:\백업도구\결과\<YYYY-MM>_verified.txt` sentinel 부재 + 매월 2일 이후 조건 만족 시 "!백업검증 필요(/백업확인)" 점등. `/백업확인` 명령에 마무리 단계로 sentinel 생성 추가 — 검증 후 자동 소거 루프 완성.
- 2026-05-19: UserPromptSubmit 훅 추가 — 박광우님 매 입력 시 "보고 톤 규약(비기술자용 일상 한국말, 결과 의미 먼저, 기술 디테일은 뒤로, 표·비유 적극 활용)" 가 시스템 콘텍스트로 자동 첨부. settings.json 변경. 메모리(`feedback_communication_tone.md`)에도 동일 정책 저장 — 이중 안전장치.
- 2026-05-19: 글로벌 슬래시커맨드 `/매일아침` 신설 (`~/.claude/commands/매일아침.md`). 매일 아침 한 줄 호출 → 케어포 점검 위험 + 평가 마감 임박 + 보고서 마감 의무 + 백업 상태 4명 에이전트 병렬 점검 → 한 페이지 화면 출력 + Gmail 초안 자동 저장. Google Cloud AI Agent Trends 2026 보고서 적용 1단계 (트렌드 1: 직원=감독자 / 트렌드 2: 다단계 조립라인).
- 2026-05-19: `/매일아침` 메일 수신 주소를 **pkw426@naver.com** 으로 변경 (Gmail에서 발신 → 네이버로 수신). 원장님 일상 확인용 주메일이 네이버 계정이라.
- 2026-05-19: 자동 메모리에 **"가족·고객 안내는 이메일로 (카톡 X)"** 결론 박음 (`projects/D------/memory/project_communication_channel_email.md`). 이유 3가지(엑셀 첨부 불가 / 템플릿 사전 승인 / 개인톡 자동화 약관 위반). 다음 세션부터 카톡 발송 옵션 자동 차단.
- 2026-05-21: 자동 메모리에 **호스트 환경 정보** 박음 (`user_host_environment_antigravity.md`) — 박광우님 PC는 Google Antigravity IDE 안에서 Claude Code를 띄워 사용. 시스템 정찰 시 Antigravity 프로세스를 수상한 흔적으로 추측하는 헛다리 패턴 방지용.
- 2026-05-19: 네이버 블로그 5월호 HTML 산출물 생성 — `C:\Users\user\Desktop\푸른초장요양원_5월블로그.html`. 5개 섹션(생신·짜장면·어버이날·손운동·단체체조) + 사진 자리표시 박스 + 해시태그. **블로그 표기 통일: "푸른초장요양원2" → "푸른초장요양원" (숫자 2 제거)** — 외부 발신용 컨텐츠에만 적용, 내부 시스템(케어포 기관기호·메모리·정책)은 그대로 "푸른초장요양원2" 유지.
- 2026-05-19: 위 블로그 HTML에 사진 5장 실제 임베드 완료. **중요 규칙 박음: 외부 공개용(블로그·홍보물)은 반드시 모자이크 처리된 PNG 사용, 모자이크 안 된 원본 JPG는 절대 사용 금지** — 어르신 개인정보 보호. 다운로드 폴더의 동일 사건 JPG/PNG 동시 존재 시 PNG가 모자이크 버전이므로 PNG 우선 선택. 사진 위치: `C:\Users\user\Desktop\푸른초장요양원_5월블로그_사진\` (1_생신잔치·2_짜장면·3_어버이날가족·4_손운동·5_단체체조 모두 .png). 마무리 섹션 문구도 새 순서에 맞춰 정리(짜장면 별식·가족 방문 포함).
