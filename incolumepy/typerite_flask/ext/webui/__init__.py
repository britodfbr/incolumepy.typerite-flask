#!/usr/bin/env python
# -*- coding: utf-8 -*-
from .main import bp

__author__ = '@britodfbr'


def init_app(app):
    app.register_blueprint(bp)
