# -*- coding: utf-8 -*-
"""
    @Time : 2022/10/7 18:31
    @Author : 李子
    @Url : https://github.com/kslz
"""
from datetime import datetime

from lizihello import db


class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    body = db.Column(db.String(200))
    timestamp = db.Column(db.DateTime, default=datetime.utcnow, index=True)
#
# from sqlalchemy.schema import CreateTable
#
# print(CreateTable(Message.__table__))