import allure
from apis.login_api import login_request


@allure.feature("认证模块")
class TestAuth:
    @allure.story("用户登录")
    @allure.title("验证正确账号密码登录成功")
    def test_login_success(self, session, base_url):
        response = login_request(session, base_url, "emilys", "emilyspass")
        assert response.status_code == 200

        res_data = response.json()
        token = res_data.get("accessToken")
        assert token is not None

        session.headers.update({"Authorization": f"Bearer {token}"})
