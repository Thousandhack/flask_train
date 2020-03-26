#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = "hsz"

from application import app
from application import manager
from flask_script import Server
import www


## web server  自定义运行命令
# app.config['SERVER_PORT'] 获取配置文件信息
manager.add_command("runserver", Server(host="0.0.0.0", port=app.config['SERVER_PORT'], use_debugger=True))


def main():
    # app.run(host="0.0.0.0", debug=True)
    manager.run()


if __name__ == '__main__':
    try:
        import sys

        sys.exit(main())
    except Exception as e:
        import traceback

        traceback.print_exc()
