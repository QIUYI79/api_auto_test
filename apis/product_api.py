def get_products_list(session, base_url, limit=10):
    """获取商品列表"""
    url = f"{base_url}/products"
    return session.get(url, params={"limit": limit}, timeout=5)


def add_to_cart(session, base_url, user_id, product_id, quantity=1):
    """添加商品到购物车"""
    # DummyJSON 的加购物车接口是 /carts/add
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
    return session.post(url, json=payload, timeout=5)

