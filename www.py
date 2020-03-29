#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = "hsz"

from application import app
from web.controllers.index import route_index
from web.controllers.user.Users import route_user
from web.controllers.static import route_static  # 为了加载静态资源添加的
from web.controllers.account.Account import route_account
from web.controllers.finance.Finance import route_finance
from web.controllers.food.Food import route_food
from web.controllers.member.Member import route_member
from web.controllers.stat.Stat import route_stat

app.register_blueprint(route_index, url_prefix="/")
app.register_blueprint(route_user, url_prefix="/user")

app.register_blueprint(route_static, url_prefix="/static")  # 为了加载静态资源添加的
# 账号管理注册
app.register_blueprint(route_account, url_prefix="/account")
# 财务管理注册
app.register_blueprint(route_finance, url_prefix="/finance")
# 美食管理
app.register_blueprint(route_food, url_prefix="/food")
# 成员管理
app.register_blueprint(route_member, url_prefix="/member")
# 统计管理
app.register_blueprint(route_stat, url_prefix="/stat")
