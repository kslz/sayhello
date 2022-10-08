# -*- coding: utf-8 -*-
"""
    @Time : 2022/10/8/008 11:25
    @Author : 李子
    @Url : https://github.com/kslz
"""
from flask_wtf import FlaskForm
from wtforms import TextAreaField, StringField, SubmitField
from wtforms.validators import DataRequired, Length


class UploadForm(FlaskForm):
    name = StringField('姓名', validators=[DataRequired(), Length(1,20)])
    body = TextAreaField('留言内容', validators=[DataRequired(), Length(1,200)])
    submit = SubmitField()