#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = "hsz"

from application import app
from web.controllers.index import route_index

app.register_blueprint(route_index, url_prefix="/")
