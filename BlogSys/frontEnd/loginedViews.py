from flask import Blueprint,render_template,url_for,request,session
from dbModel.modelclass import User,userZip
from configuration import app,db,login_required,logout_user,login_user
import os


logined=Blueprint('logined',__name__)
# loginMan.init_app(app)  #应用去关联登录框架
# dbOpt=SQLAlchemy(app)   #应用去关联数据库
app.config['UPLOAD_FOLDER']=os.getcwd()+"/static/uploads"#配置文件上传的路径为当前的目录
#上传文件格式
filetype=['txt','jpg','gif','png','dll','rar','zip','mp4','avi', 'mpg' ,'rmvb','mp3','wav','swf','wps']
#主页面
# 登录后页面视图函数
@logined.route('/aa')
def loginobj():
    '''登录页视图'''
    return render_template('loginedpage.html')
    pass

#过滤器
def guolv(filename):
    if '.' in filename and filename.rsplit('.',1)[1] in filetype:
        return True
    else:
        return False

@logined.route('/up',methods=['post'])
def upBlog():
    if request.method == 'POST':
        fileobj = request.files['file']  # 获取标签对象
        try:
            if guolv(fileobj.filename):
                fileobj.save(os.path.join(app.config['UPLOAD_FOLDER'], fileobj.filename))
                file_url = url_for('static', filename='/www'+ fileobj.filename)
                return fileobj.filename
        except Exception as e:
                return '格式错误,请重新上传'
        return render_template('loginedpage.html')

@logined.route('/static/www/<url>')
def aaa(url):
    return render_template('loginedpage.html', path=url)


@logined.route('/logout')
def loginout():
    '''登出'''
    logout_user()
    return '已退出'

# if __name__ == '__main__':
#     app.config['JSON_AS_ASCII']=False
#     app.run()