# 数据库表的创建
from flask_login import UserMixin
from configuration import db

class User(db.Model,UserMixin):
    __tablename__='User'
    userId=db.Column(db.Integer,primary_key=True)
    userInfo=db.Column(db.String(20))
    userPwd=db.Column(db.Integer)
    userPhone=db.Column(db.Integer)
    userzip=db.relationship('userZip')
    def __init__(self,userId,userInfo,userPwd,userPhone):
        self.userId=userId
        self.userInfo=userInfo
        self.userPwd=userPwd
        self.userPhone=userPhone

class userZip(db.Model,UserMixin):
    __tablename__='userZip'
    id=db.Column(db.Integer,primary_key=True)
    usermsg=db.Column(db.String(100))
    img_name=db.Column(db.String(40))
    img=db.Column(db.LargeBinary(length=2048))
    userId=db.Column(db.Integer,db.ForeignKey('User.userId'))
    def __init__(self,id,usermsg,img_name,img,userId):
        self.id=id
        self.usermsg=usermsg
        self.img_name=img_name
        self.img=img
        self.userId=userId