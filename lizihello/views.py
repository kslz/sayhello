# -*- coding: utf-8 -*-
"""
    @Time : 2022/10/8/008 11:29
    @Author : 李子
    @Url : https://github.com/kslz
"""
from flask import flash, url_for, redirect, render_template

from lizihello import app, db
from lizihello.forms import UploadForm
from lizihello.models import Message


@app.route('/',methods=['GET', 'POST'])
def index():
    form = UploadForm()
    if form.validate_on_submit():
        name = form.name.data
        body = form.body.data
        message = Message(body=body, name=name)
        db.session.add(message)
        db.session.commit()
        flash('您的消息已提交')
        return redirect(url_for('index'))

    messages = Message.query.order_by(Message.timestamp.desc()).all()
    return render_template('index.html', messages=messages, form=form)

