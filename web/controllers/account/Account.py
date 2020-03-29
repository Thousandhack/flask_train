#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = "hsz"


from flask import Blueprint, render_template

# 给模块配置路由  index_user 不同模块命名不同
route_account = Blueprint('account_page', __name__)


# 需要将路由注册到www.py文件夹下才能生效

@route_account.route("/index")
def index():
    return render_template("account/index.html")


@route_account.route("/info")
def info():
    return render_template("account/info.html")


@route_account.route("/set")
def set():
    return render_template("account/set.html")