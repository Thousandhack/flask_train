#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = "HSZ"

SERVER_PORT = 8800

SQLALCHEMY_ECHO = False

SQLALCHEMY_DATABASE_URI = 'mysql://root:123456@127.0.0.1/flask_train?charset=utf8mb4'

SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_ENCODING = "utf8mb4"

AUTH_COOKIE_NAME = "hsz"

# 过滤url
IGNORE_URLS = [
    "^/user/login"
]

IGNORE_CHECK_LOGIN_URLS = [
    "^/static",
    "^/favion.ico"
]
