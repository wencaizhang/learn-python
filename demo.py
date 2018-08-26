# 从 flask 这个框架中导入 Flask 这个类
from flask import Flask, redirect, url_for
import config

# 初始化一个 Flask 对象
# Flask() 需要传递一个参数 __name__
# 1. 方便 flask 框架寻找资源
# 2. 方便 flask 插件比如 Flask-sqlalchemy 出现错误的时候寻找问题所在的位置
app = Flask(__name__)
app.config.from_object(config)


# @app.route 是一个装饰器
# @开头，并且在函数上面，就说明是一个装饰器
# 这个装饰器的作用是做一个 url 和视图函数的映射
# 访问指定的 url，会请求 hello_world 函数，并将结果返回给浏览器
@app.route('/')
def hello_world():
    print('my_list')

    # 重定向到登录页面
    login_url = url_for('login')
    return redirect(login_url)
    return 'Hello, World!'


@app.route('/article/<id>')
def article(id):
    return u'您请求的参数是： %s' % id


@app.route('/list')
def my_list():
    return 'list'


@app.route('/login')
def login():
    return '请您先登录'


# 如果当前这个文件是作为入口程序执行，就会执行 app.run()
if __name__ == '__main__':
    # 启动一个应用服务器，来接受用户的请求
    app.run()
