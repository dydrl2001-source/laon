"""공통 Windows 토스트 알림 도구 — 모든 자동화 프로젝트가 산출물 생성 직후 호출.

박광우님 화면 우하단에 알림이 뜨고, 본체 클릭 시 산출물 파일이 즉시 열림.
주식 프로젝트(cli/daily.py)의 _send_toast_notification 패턴을 일반화한 공용 버전.

사용법 (Python):
    from notify import send_toast
    send_toast(
        app_id="🏥 케어포 점검",
        title="✅ 오늘 일일 점검 완료",
        message="15:30 생성 — 클릭하면 엑셀이 열립니다.",
        file_path="D:/carefor_checker_saas/output/reports/daily/check_report_프리미엄_20260519.xlsx",
        folder_path="D:/carefor_checker_saas/output/reports/daily/",
        alert_level="info",   # "info" | "warning" | "critical"
    )

사용법 (PowerShell / 배치):
    python "D:\\메인작업\\tools\\notify.py" `
        --app-id "💾 백업도구" `
        --title "이번 달 백업 완료" `
        --message "ZIP 9개 + 미러 갱신" `
        --file "D:\\백업도구\\결과\\2026-06-01\\" `
        --level info

의존성:
    winotify >= 1.1, < 2.0  (없으면 조용히 스킵 — 산출물 생성은 절대 안 막음)
    설치: pip install winotify
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path


_LEVEL_PREFIX = {
    "info": "",
    "warning": "⚠️ ",
    "critical": "🚨 ",
}


def send_toast(
    app_id: str,
    title: str,
    message: str = "",
    file_path: str | Path | None = None,
    folder_path: str | Path | None = None,
    alert_level: str = "info",
) -> bool:
    """Windows 토스트 알림을 띄운다. 성공 시 True, 실패 시 False.

    winotify 미설치 또는 알림 실행 실패 시 조용히 False 반환. 호출 측의
    작업 흐름을 절대 막지 않는 게 핵심 원칙.
    """
    try:
        from winotify import Notification, audio
    except ImportError:
        return False

    prefix = _LEVEL_PREFIX.get(alert_level, "")
    full_title = f"{prefix}{title}" if prefix else title

    try:
        kwargs = {
            "app_id": app_id,
            "title": full_title,
            "msg": message,
            "duration": "long",
        }
        if file_path:
            kwargs["launch"] = str(file_path)

        toast = Notification(**kwargs)
        toast.set_audio(audio.Default, loop=False)

        if folder_path:
            toast.add_actions(label="📂 폴더 열기", launch=str(folder_path))

        toast.show()
        return True
    except Exception:
        return False


def _cli(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="공통 Windows 토스트 알림 — 자동화 프로젝트 산출물 완료 알림용",
    )
    parser.add_argument("--app-id", required=True, help="알림 발신자 표시 (예: '💾 백업도구')")
    parser.add_argument("--title", required=True, help="알림 제목")
    parser.add_argument("--message", default="", help="알림 본문")
    parser.add_argument("--file", dest="file_path", default=None, help="알림 클릭 시 열 파일 경로")
    parser.add_argument("--folder", dest="folder_path", default=None, help="'📂 폴더 열기' 보조 액션 대상")
    parser.add_argument(
        "--level",
        dest="alert_level",
        default="info",
        choices=["info", "warning", "critical"],
        help="알림 등급 (warning=⚠️ / critical=🚨)",
    )
    args = parser.parse_args(argv)

    ok = send_toast(
        app_id=args.app_id,
        title=args.title,
        message=args.message,
        file_path=args.file_path,
        folder_path=args.folder_path,
        alert_level=args.alert_level,
    )
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(_cli())
