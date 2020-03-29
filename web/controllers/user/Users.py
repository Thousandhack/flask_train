#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = "hsz"

from flask import Blueprint, render_template
from flask import request
from flask import jsonify
from common.models.user import User
# 给模块配置路由  index_user 不同模块命名不同
route_user = Blueprint('index_user', __name__)


# 需要将路由注册到www.py文件夹下才能生效

@route_user.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == "GET":
        return render_template("/user/login.html")
    elif request.method == "POST":
        resp = {'code': 0, 'msg': '登录成功', 'data': {}}
        req = request.values
        login_name = req['login_name'] if 'login_name' in req else ''
        login_pwd = req['login_pwd'] if 'login_pwd' in req else ''

        if login_name is None or len(login_name) < 1:
            resp['code'] = -1
            resp['msg'] = '登录失败，用户名不正确'
            return jsonify(resp)

        if login_pwd is None or len(login_pwd) < 1:
            resp['code'] = -1
            resp['msg'] = '登录失败，请输入正确的密码！'
            return jsonify(resp)

        user_info = User.query.filter_by(login_name=login_name).first()

        if not user_info:
            resp['code'] = -1
            resp['msg'] = '请输入正确的登录用户名和密码！'
            return jsonify(resp)
        return "%s %s" % (login_name, login_pwd)


@route_user.route("/edit")
def edit():
    return render_template("/user/edit.html")


@route_user.route("/reset-pwd")
def reset_pwd():
    return render_template("/user/reset_pwd.html")
