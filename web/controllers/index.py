#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = "hsz"
# 使用蓝图
from flask import Blueprint,render_template

route_index = Blueprint('index_page', __name__)


@route_index.route("/")
def index():
    return render_template("/index/index.html")
