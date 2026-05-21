# hooks/ — Claude Code 하네스 훅 스크립트

`~/.claude/settings.json`의 hooks/statusLine 항목이 호출하는 PowerShell 스크립트 모음. 거버넌스 정책을 **자연어 약속이 아닌 시스템 차단**으로 강제하는 하네스 엔지니어링 레이어.

## 스크립트 목록

| 파일 | 호출 시점 | 역할 |
|---|---|---|
| `block_off_project_writes.ps1` | PreToolUse · Write\|Edit | **대칭 격리**: 현재 CWD가 `manifest.yaml` 등록 프로젝트에 속하면 "내 프로젝트 내부"만 쓰기 허용, 그 외 D:\ 경로는 차단. 비-D 경로·미등록 CWD는 통과. 메인작업/주식/블로그자동화 등 모든 등록 프로젝트가 양방향 보호받음 (3대 금지선 #1 격상) |
| `statusline.ps1` | 상태표시줄 (refreshInterval) | `[폴더] [governance/RO] | D:?GB | 1관/2관 확인 | !백업검증 필요` 표시. 당월 2일 이후 + `D:\백업도구\결과\<YYYY-MM>_verified.txt` 부재 시 검증 리마인더 점등 |

## 작성 규약

- **shell**: `pwsh` (PowerShell 7+, `$ErrorActionPreference` 명시)
- **stdin**: `[Console]::In.ReadToEnd() | ConvertFrom-Json`로 페이로드 수신
- **PreToolUse 차단**: `hookSpecificOutput.permissionDecision = "deny"` JSON 출력 (exit 2 대신)
- **statusLine**: 한 줄 plain text 출력 (이모지 없이)
- **인코딩**: UTF-8 (한글 메시지 포함)

## 수동 테스트 (pipe-test)

```powershell
# 1. 차단되어야 함 (메인작업 CWD → 다른 D 프로젝트 수정 시도)
'{"tool_name":"Edit","tool_input":{"file_path":"D:\\블로그자동화\\test.py"},"cwd":"D:\\메인작업"}' | pwsh -NoProfile -File "D:\메인작업\hooks\block_off_project_writes.ps1"

# 2. 통과해야 함 (메인작업 내부 수정)
'{"tool_name":"Edit","tool_input":{"file_path":"D:\\메인작업\\CLAUDE.md"},"cwd":"D:\\메인작업"}' | pwsh -NoProfile -File "D:\메인작업\hooks\block_off_project_writes.ps1"

# 3. 차단되어야 함 (대칭 격리 — 주식 CWD → 블로그 수정 시도)
'{"tool_name":"Edit","tool_input":{"file_path":"D:\\블로그자동화\\test.py"},"cwd":"D:\\주식"}' | pwsh -NoProfile -File "D:\메인작업\hooks\block_off_project_writes.ps1"

# 4. 통과해야 함 (주식 CWD → 주식 내부)
'{"tool_name":"Edit","tool_input":{"file_path":"D:\\주식\\src\\bridge\\client.py"},"cwd":"D:\\주식"}' | pwsh -NoProfile -File "D:\메인작업\hooks\block_off_project_writes.ps1"

# 5. 통과해야 함 (어떤 CWD든 비-D 경로는 자유)
'{"tool_name":"Edit","tool_input":{"file_path":"C:\\Users\\user\\.claude\\settings.json"},"cwd":"D:\\주식"}' | pwsh -NoProfile -File "D:\메인작업\hooks\block_off_project_writes.ps1"

# 상태표시줄 출력 확인
'{"workspace":{"current_dir":"D:\\메인작업"}}' | pwsh -NoProfile -File "D:\메인작업\hooks\statusline.ps1"
```

## settings.json 등록 위치

`~/.claude/settings.json` (글로벌 — 모든 세션 적용)
- `hooks.PreToolUse`: matcher `Write|Edit` → `block_off_project_writes.ps1`
- `statusLine`: command 직접 호출

훅 변경 후 Claude Code가 인식하려면 `/hooks` 메뉴 한 번 열거나 세션 재시작 필요.

## 변경 이력

- 2026-05-09: 초기 2종 (`block_off_project_writes.ps1` / `statusline.ps1`) — 하네스 엔지니어링 Tier 1 적용
- 2026-05-11: statusline에 매월 백업검증 리마인더 추가. `/백업확인` 성공 시 sentinel 파일 생성 → 알림 자동 소거 (Tier 2 옵션 B 적용)
- 2026-05-13: `block_off_project_writes.ps1` 대칭 격리로 확장 — 메인작업 단방향 → N-방향. `manifest.yaml` projects[*].path 파싱해 등록 프로젝트면 모두 "내 경로만 허용" 규칙 적용. D:\주식 등 모든 신규 프로젝트가 자동으로 양방향 보호받음. manifest 읽기 실패 시 기존 메인작업 단방향으로 폴백.
