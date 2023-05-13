from typing import Optional

import httpx
import json

BASE_URL = 'http://localhost:8000/'


def get_category():
    url = f'{BASE_URL}/categories'
    response = httpx.get(url=url).json()
    return response


def get_product():
    url = f'{BASE_URL}/products'
    response = httpx.get(url=url).text
    data = json.loads(response)
    return data


def add_user(id, first_name, username):
    url = f'{BASE_URL}/user'
    response = httpx.get(url=url).json()
    user_exist = False
    for i in response:
        if i['username'] == username:
            user_exist = True
            break
    if user_exist:
        return 'this user already exist'
    httpx.post(url=url, data={'id': id, 'first_name': first_name, 'username': username})
    return 'user added success'


def create_category(name):
    url = f'{BASE_URL}/categories'
    response = httpx.get(url=url).text
    data = json.loads(response)
    category_exist = False
    for i in data:
        if i['name'] == name:
            category_exist = True
            break
    if category_exist == False:
        post = httpx.post(url=url, data={'name': name})
        return 'created category'
    else:
        return 'category already exist'


def create_product(name: str, description: str, category: int):
    url = f'{BASE_URL}/products'
    if name and category:
        post = httpx.post(url, data={'name': name, 'description': description, 'category': category})
        return "product added successfully"
    else:
        return "error"


