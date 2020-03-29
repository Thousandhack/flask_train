#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = "hsz"

from flask import Flask
from flask_script import Manager
from flask_sqlalchemy import SQLAlchemy

import os


class Application(Flask):

    def __init__(self, import_name, template_folder=None, root_path=None):
        """

        :param import_name:
        :param template_folder: 模板文件
        :param root_path: 根目录
        """
        super(Application, self).__init__(import_name, template_folder=template_folder, root_path=root_path,
                                          static_folder=None)
        self.config.from_pyfile('config/settings.py')  # 配置文件
        # if "os_config" in os.environ:
        #     self.config.from_pyfile('config/%s_settings.py' % os.environ['os_config'])
        db.init_app(self)  # 初始化


db = SQLAlchemy()
app = Application(__name__, template_folder=os.getcwd() + "/web/templates/", root_path=os.getcwd())
app.config['JSON_AS_ASCII'] = False  # 正常返回中文的配置
manager = Manager(app)


"""
函数模板
"""
from common.libs.UrlManager import UrlManager

app.add_template_global(UrlManager.buildStaticUrl, 'buildStaticUrl')
app.add_template_global(UrlManager.buildUrl, 'buildUrl')
