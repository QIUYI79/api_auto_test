def login_request(session, base_url, username, password):

    url = f"{base_url}/auth/login"

    payload = {
        'username': username,
        'password': password,
        'expiresINMInMins': 30
    }

    return session.post(url, json=payload, timeout=5)
