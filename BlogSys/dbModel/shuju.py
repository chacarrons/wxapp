from flask_login import UserMixin
from configuration import dbContext,loginManger


class User(dbContext.Model,UserMixin):  #关联存储session对象的数据模型类
    __tablename__='user'
    id=dbContext.Column(dbContext.Integer,primary_key=True)
    account=dbContext.Column(dbContext.String(20))

class ActicleList(dbContext.Model):
    __tablename__='ActicleList'
    id=dbContext.Column(dbContext.Integer,primary_key=True)
    account=dbContext.Column(dbContext.String(20))