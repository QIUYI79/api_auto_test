import requests


def get_current_user_info(session, base_url):
    """获取当前登录用户的信息"""
    url = f"{base_url}/auth/me"
    return session.get(url, timeout=5)
