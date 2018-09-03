# 首页视图
from flask import render_template
from configuration import app
from frontEnd.homeViews import *
from frontEnd.loginedViews import *
import logging
app.register_blueprint(home,url_prefix='/home')
app.register_blueprint(logined,url_prefix='/logined')

@app.route('/')
def hello_world():
    return render_template('homepage.html')


if __name__ == '__main__':
    app.run()
