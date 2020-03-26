#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = "hsz"

from flask import Flask
from flask_script import Manager
from flask_sqlalchemy import SQLAlchemy


# import os

class Application(Flask):
    def __init__(self, import_name):
        super(Application, self).__init__(import_name)
        self.config.from_pyfile('config/settings.py')  # 配置文件
        # if "os_config" in os.environ:
        #     self.config.from_pyfile('config/%s_settings.py' % os.environ['os_config'])
        db.init_app(self)  # 初始化


db = SQLAlchemy()
app = Application(__name__)
manager = Manager(app)
