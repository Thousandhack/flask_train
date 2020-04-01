#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = "hsz"

from application import app
from flask import request, redirect,g
from common.models.user import User
from common.libs.user.UserService import UserService
from common.libs.UrlManager import UrlManager
import re


@app.before_request
def before_request():
    # 跳过这些url的登录验证
    ignore_urls = app.config['IGNORE_URLS']
    ignore_check_login_urls = app.config['IGNORE_CHECK_LOGIN_URLS']
    path = request.path
    user_info = check_login()

    # 如果是静态文件就不要查询用户信息了
    pattern = re.compile('%s' % "|".join(ignore_check_login_urls))
    if pattern.match(path):
        return

    if '/api' in path:
        return

    user_info = check_login()
    g.current_user = None

    if not user_info:
        return redirect(UrlManager.buildUrl("/user/login"))

    return


def check_login():
    """
    判断用户是否登录
    :return:
    """
    cookies = request.cookies
    auth_cookie = cookies[app.config['AUTH_COOKIE_NAME']] if app.config['AUTH_COOKIE_NAME'] in cookies else None

    if auth_cookie is None:
        return False

    auth_info = auth_cookie.split("#")  # 根据Users.py中的#来的
    if len(auth_info) != 2:
        return False

    try:
        user_info = User.query.filter_by(uid=auth_info[1]).first()
    except Exception:
        return False

    if user_info is None:
        return False

    if auth_info[0] != UserService.geneAuthCode(user_info):
        return False

    if user_info.status != 1:
        return False

    return user_info
