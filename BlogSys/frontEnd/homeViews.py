
from flask import Blueprint,render_template,url_for,request,session,flash
from functools import wraps
from dbModel.modelclass import User,userZip
from configuration import app,db,login_required,logout_user,login_user


home=Blueprint('home',__name__)#创建一个蓝图对象
# 主页视图函数





# @home.route('/home')
# @login_required
# def homeobj():
#     return render_template('homepage.html')
#     pass

@home.route('/register',methods=['get','post'])
def register():
    '''注册'''
    db.create_all()
    try:
        if request.method=='POST':
            userinfo=request.form['userInfo']
            userpwd=request.form['userPwd']
            userphone=request.form['userPhone']
            userobj=User.query.filter_by(userInfo=userinfo).first()
            userlist = [userinfo, userpwd, userphone]
            if userobj is not None:
                return flash('账号已存在，请重新注册')
            else:
                newuser=User(userlist[0],userlist[1],userlist[2])
                db.session.add(newuser)
                db.session.commit()
                return flash('注册成功')
    except Exception as a:
        app.logger.error(a)
    finally:
        db.session.close()
        pass
    # return render_template('homepage.html')



@home.route('/login',methods=['get','post'])
def login():
    '''登录'''
    try:
        if request.method == 'POST':
            # userId = request.form['userId']
            usinfo = request.form['userInfo']
            uspwd=request.form['userPwd']
            usobj=User.query.filter_by(userInfo=usinfo,userPwd=uspwd).first()
            if usobj is not None:
                login_user(usobj, True)  # 将登录的对象保存在框架的session中
                return render_template('loginedpage.html')
            else:
                return flash('登录失败')
                pass
    except Exception as ex:
        app.logger.error(ex)
    return render_template('homepage.html')



@app.errorhandler(404)
def pagenot(e):
    '''404页面视图'''

    return render_template('404.html')

