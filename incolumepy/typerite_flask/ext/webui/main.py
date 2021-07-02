#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Blueprint, request, render_template

__author__ = '@britodfbr'


bp = Blueprint('site', __name__)


@bp.route('/')
def index():
    return render_template(
        'index.html',
        name=request.args.get('name', 'visitante')
    )
