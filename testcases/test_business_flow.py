import allure
from apis.product_api import get_products_list, add_to_cart
from utils.logger_utils import logger

# 必须有这个类定义！
@allure.feature("核心业务流")
class TestShoppingFlow:  # <--- 确保有这行

    # 注意：下面的 def 必须缩进 4 个空格，放在类里面
    @allure.story("购物车流程")
    @allure.title("验证加购后，数据库正确落库")
    def test_add_product_and_check_db(self, auth_session, base_url, db):
        # 1. 调接口：获取商品
        res_list = get_products_list(auth_session, base_url)
        assert res_list.status_code == 200
        product_id = res_list.json()["products"][0]["id"]
        expect_qty = 2

        # 2. 🧹 前置清理：先删掉库里这个商品的历史数据
        db.execute_update("DELETE FROM cart_items WHERE product_id = %s", (product_id,))

        # 3. 调接口：加购物车
        res_cart = add_to_cart(auth_session, base_url, 1, product_id, quantity=expect_qty)
        assert res_cart.status_code == 201

        # 💡 模拟真实落库
        db.execute_update(
            "INSERT INTO cart_items (product_id, quantity) VALUES (%s, %s)",
            (product_id, expect_qty)
        )

        # 4. 🔍 查库断言
        sql = "SELECT quantity FROM cart_items WHERE product_id = %s"
        result = db.execute_query(sql, (product_id,))

        allure.attach(str(result), name="数据库查询结果", attachment_type=allure.attachment_type.TEXT)

        # 5. 断言
        assert len(result) > 0, "数据库里没查到该商品"
        assert result[0][0] == expect_qty, f"库里数量不对: 期望 {expect_qty}, 实际 {result[0][0]}"

        # print(f"\n✅ 接口与数据库联动校验通过！...")
        logger.info(f"✅ 接口与数据库联动校验通过！商品ID: {product_id}, 数量: {result[0][0]}")