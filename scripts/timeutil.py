#!/usr/bin/env python3
"""统一使用上海时间（Asia/Shanghai, UTC+8）。"""
from __future__ import annotations

from datetime import datetime, timezone, timedelta
from typing import Any

# 上海无夏令时，固定 +08:00 足够；优先 zoneinfo
try:
    from zoneinfo import ZoneInfo

    SHANGHAI = ZoneInfo("Asia/Shanghai")
except Exception:  # pragma: no cover
    SHANGHAI = timezone(timedelta(hours=8))

CST = SHANGHAI  # 别名


def now_shanghai() -> datetime:
    return datetime.now(SHANGHAI)


def now_iso() -> str:
    """ISO8601，带 +08:00。"""
    return now_shanghai().isoformat(timespec="seconds")


def now_iso_ms() -> str:
    return now_shanghai().isoformat()


def parse_dt(value: Any) -> datetime | None:
    if value is None:
        return None
    if isinstance(value, datetime):
        dt = value
    else:
        s = str(value).strip()
        if not s:
            return None
        # 兼容 Z
        if s.endswith("Z"):
            s = s[:-1] + "+00:00"
        try:
            dt = datetime.fromisoformat(s)
        except Exception:
            return None
    if dt.tzinfo is None:
        # 无时区的按 UTC 理解（Actions 常见）再转上海
        dt = dt.replace(tzinfo=timezone.utc)
    return dt.astimezone(SHANGHAI)


def to_shanghai_iso(value: Any = None, timespec: str = "seconds") -> str:
    dt = parse_dt(value) if value is not None else now_shanghai()
    if dt is None:
        dt = now_shanghai()
    return dt.isoformat(timespec=timespec)


def to_shanghai_display(value: Any = None) -> str:
    """人类可读：2026-08-04 04:01:48 CST"""
    dt = parse_dt(value) if value is not None else now_shanghai()
    if dt is None:
        dt = now_shanghai()
    return dt.strftime("%Y-%m-%d %H:%M:%S CST")


def to_shanghai_badge(value: Any = None) -> str:
    """badge 短格式：2026-08-04_04:01:48（空格已不宜，render 里再处理）"""
    dt = parse_dt(value) if value is not None else now_shanghai()
    if dt is None:
        dt = now_shanghai()
    return dt.strftime("%Y-%m-%d %H:%M:%S")
