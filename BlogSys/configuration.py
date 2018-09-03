# 配置管理
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager,login_user,logout_user,current_user,UserMixin,login_required
from flask import Flask
# from frontEnd.homeViews import home
import logging
app = Flask(__name__)
app.config['SECRET_KEY']='a'
app.config['SQLALCHEMY_DATABASE_URI']='mysql://root:111111@localhost:3306/user'#连接数据库
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
dbContext=SQLAlchemy(app)
loginManger=LoginManager(app)

db=SQLAlchemy(app)

# app.register_blueprint(home,url_prefix='/home')

loginManger=LoginManager(app)
# 默认的登录页面
loginManger.login_view='/login'
# 设置记录session的强度  none  basic strong
loginManger.session_protection='strong'
# 登陆对象去关联用户
loginManger.init_app(app)
# 创建日志文件
loghandler=logging.FileHandler('error.log',encoding='utf-8')
# 日志格式
loggingFormat=logging.Formatter(
       '%(asctime)s - %(levelname)s - %(filename)s - %(funcName)s - %(lineno)s - %(message)s'
)
#将日志格式绑定到日志管理对象
loghandler.setFormatter(loggingFormat)

# 关联日志对象
app.logger.addHandler(loghandler)