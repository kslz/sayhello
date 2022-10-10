# -*- coding: utf-8 -*-
"""
    @Time : 2022/10/7 18:31
    @Author : 李子
    @Url : https://github.com/kslz
"""
import click
from flask import Flask
from flask_bootstrap import Bootstrap
from flask_debugtoolbar import DebugToolbarExtension
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy

app = Flask('lizihello')
app.config.from_pyfile('settings.py')
app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True

db = SQLAlchemy(app)
bootstrap = Bootstrap(app)
moment = Moment(app)

from lizihello import views, commands

toolbar = DebugToolbarExtension(app)




