# MCP 서버 구성 정책

## 글로벌 MCP 등록 위치

- 파일: `~/.claude/.mcp.json` (모든 Claude Code 세션 자동 적용)
- 백업: `~/.claude/.mcp.json.backup-YYYYMMDD-HHMMSS` (변경 시 생성 권장)

## 현재 등록된 MCP 서버 (5개, 2026-05-01 기준)

| 서버 이름 | 출처 | 비고 |
|---|---|---|
| `notebooklm` | npx notebooklm-mcp | 평가매뉴얼 노트북 자문 |
| `pdf-viewer` | ant.dir.gh.anthropic.pdf-server-mcp | Anthropic 공식 PDF 뷰어 |
| `figma` | ant.dir.ant.figma.figma | Figma Desktop Dev Mode 켜져 있어야 동작 |
| `pdf-toolkit` | ant.dir.gh.silverstein.pdf-filler-simple | PDF 폼/병합/분할, env 경로 `Documents`·`~/.pdf-toolkit-files` |
| `desktop-commander` | ant.dir.gh.wonderwhy-er.desktopcommandermcp | 파일/터미널 광범위 — Claude Code 기본 도구와 중복 가능 |

## 신규 MCP 추가 패턴

```json
{
  "mcpServers": {
    "<이름>": {
      "command": "node",
      "args": ["<설치경로>/<entry>.js"],
      "env": { "<KEY>": "<VALUE>" }
    }
  }
}
```

## Claude Desktop 확장 임포트

Desktop 설치 위치:
`C:/Users/user/AppData/Local/Packages/Claude_pzs8sxrjxfjjc/LocalCache/Roaming/Claude/Claude Extensions/<id>/`

각 확장의 `manifest.json`에서 `server.entry_point` 확인 후 절대경로로 등록.

## claude.ai 커넥터

웹 claude.ai에서 연결한 커넥터(Gmail/Calendar/Drive/S&P Global)는 Claude Code에 자동 전파됨 (`mcp__claude_ai_*` 도구로 노출). 별도 설정 불필요.

**Adobe 커넥터**: 화이트리스트 미통과 — claude.ai 웹 전용. Claude Code에서 사용 불가.

## 깨진 MCP 진단

- 세션 시작 시 `/mcp` 명령으로 connection 상태 확인
- `mcp-needs-auth-cache.json` 확인 (인증 필요한 서버)
- Desktop이 확장 제거/업데이트 시 경로 변동 가능 → manifest.json 재확인 후 갱신
