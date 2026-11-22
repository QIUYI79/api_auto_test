import allure
from apis.user_api import get_current_user_info


@allure.feature("用户管理模块")
class TestUser:

    @allure.story("获取当前用户信息")
    @allure.title("验证登录后能成功获取个人详情")
    def test_get_current_user(self, auth_session, base_url):
        response = get_current_user_info(auth_session, base_url)

        # 魔法1：将完整响应报文挂载为附件
        allure.attach(
            response.text,
            name="接口完整响应报文",
            attachment_type=allure.attachment_type.JSON
        )

        assert response.status_code == 200
        user_data = response.json()
        assert user_data["username"] == "emilys"

        # 魔法2：将关键业务数据（邮箱）挂载为附件
        allure.attach(
            user_data['email'],
            name="当前登录用户邮箱",
            attachment_type=allure.attachment_type.TEXT
        )
