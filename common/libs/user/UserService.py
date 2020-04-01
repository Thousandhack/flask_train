#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = "hsz"
import hashlib, base64
import random
import string


class UserService():

    @staticmethod  # 静态方法
    def geneAuthCode(user_info=None):
        """
        产生一个授权码
        :param user_info:
        :return:
        """
        m = hashlib.md5()
        str = "%s-%s-%s-%s" % (user_info.uid, user_info.login_name, user_info.login_pwd, user_info.login_salt)
        m.update(str.encode("utf-8"))
        return m.hexdigest()

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

    @staticmethod
    def geneSalt(length=16):
        keylist = [random.choice((string.ascii_letters + string.digits)) for i in range(length)]
        return ("".join(keylist))
