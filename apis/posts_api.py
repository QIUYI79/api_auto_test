import requests


def get_posts_request(base_url):
    url = f'{base_url}/posts'
    return requests.get(url, timeout=5)


def create_post_request(base_url, payload):
    url = f'{base_url}/posts'
    return requests.post(url, json=payload, timeout=5)
