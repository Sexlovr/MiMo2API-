"""会话管理 — 每次请求创建新会话（强制 Context Dump）"""

import uuid

def get_or_create_session(
    account_id: str,
    messages: list,
    model: str = "mimo-v2-pro",
) -> tuple:
    """获取或创建会话。现已修改为：每次请求都创建全新的会话，确保不复用旧 chat。"""
    return uuid.uuid4().hex[:32], True


def update_fingerprint(account_id: str, conversation_id: str, messages: list) -> None:
    """跳过指纹更新。"""
    pass


def update_tokens(account_id: str, conversation_id: str, prompt_tokens: int) -> None:
    """跳过 token 计数更新。"""
    pass


def get_expired_sessions(account_id: str = None, ttl: int = 0) -> list:
    """返回空列表，不再有过期会话记录。"""
    return []


def remove_session(account_id: str, conversation_id: str) -> None:
    """跳过移除操作。"""
    pass
