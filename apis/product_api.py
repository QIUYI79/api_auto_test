from utils.logger_utils import logger


def get_products_list(session, base_url, limit=10):
    """获取商品列表"""
    url = f"{base_url}/products"

    # 新增：记录请求日志
    logger.info(f"发起获取商品列表请求: URL={url}, 参数: limit={limit}")

    response = session.get(url, params={"limit": limit}, timeout=5)

    # 新增：记录响应日志
    logger.info(f"获取商品列表响应: 状态码={response.status_code}")

    return response


def add_to_cart(session, base_url, user_id, product_id, quantity=1):
    """添加商品到购物车"""
    url = f"{base_url}/carts/add"
    payload = {
        "userId": user_id,
        "products": [
            {
                "id": product_id,
                "quantity": quantity
            }
        ]
    }

    # 新增：记录请求日志（把 payload 也打出来，方便排查参数错误）
    logger.info(f"发起加购物车请求: URL={url}, 请求体={payload}")

    response = session.post(url, json=payload, timeout=5)

    # 新增：记录响应日志（如果是报错，看响应体就能知道原因）
    logger.info(f"加购物车响应: 状态码={response.status_code}")

    return response