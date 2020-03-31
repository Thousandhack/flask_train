#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = "hsz"
import hashlib, base64


class UserService():

    @staticmethod
    def genPwd(pwd, salt):
        """
        一个md5的使用
        :param pwd:
        :param salt:
        :return:
        """
        m = hashlib.md5()
        # 加密密码 加盐 加密
        str = "%s-%s" % (base64.encodebytes(pwd.encode("utf-8")), salt)
        m.update(str.encode("utf-8"))
        return m.hexdigest()
