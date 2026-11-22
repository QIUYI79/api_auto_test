import pytest
import requests
from utils.db_utils import DBUtils


@pytest.fixture(scope='session')
def base_url():
    return "https://dummyjson.com"


@pytest.fixture(scope='session')
def session():
    """创建一个全局的 session 的实例"""
    with requests.Session() as s:
        yield s


@pytest.fixture(scope='session')
def auth_session(session, base_url):

    """
    带鉴权的 session。
    依赖基础 session 和 base_url， 自动执行登录流程。
    """
    url = f"{base_url}/auth/login"
    payload = {
        "username": "emilys",
        "password": "emilyspass",
        "expiresInMins": 30
    }
    response = requests.post(url, json=payload, timeout=5)

    token = response.json().get('accessToken')

    session.headers.update({'Authorization': f'Bearer {token}'})

    return session


@pytest.fixture(scope="function")
def db():
    """提供数据库连接，用例结束后自动关闭"""
    db_obj = DBUtils()
    yield db_obj
    db_obj.close()

