#encoding: utf-8

# 从 flask 这个框架中导入 Flask 这个类
from flask import Flask, request, jsonify, url_for, redirect
# from flask_sqlalchemy import SQLAlchemy
import config
import json

# 初始化一个 Flask 对象
# Flask() 需要传递一个参数 __name__
# 1. 方便 flask 框架寻找资源
# 2. 方便 flask 插件比如 Flask-sqlalchemy 出现错误的时候寻找问题所在的位置
app = Flask(__name__)
app.config.from_object(config)

# 初始化数据库
# db = SQLAlchemy(app)

# db.create_all()

# @app.route 是一个装饰器
# @开头，并且在函数上面，就说明是一个装饰器
# 这个装饰器的作用是做一个 url 和视图函数的映射
# 访问指定的 url，会请求 hello_world 函数，并将结果返回给浏览器
@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/api/login', methods=['POST'])
def login():
    data = request.get_data()
    json_data = json.loads(data.decode("utf-8"))
    username = json_data.get('username')
    password = json_data.get('password')
    if username != 'admin' or password != '888888':
        return jsonify({ 
            'code': -1,
            'message': '账户名或密码错误（admin/888888）',
        })
    else:
        return jsonify({ 
            'code': 0,
            'message': '欢迎回来',
            'data': {
                'user': { 
                    'name': username,
                    'avatar': 'https://images.gitee.com/uploads/67/928967_wencaizhang.png?1534395755',
                }, 
            }
        })


# 如果当前这个文件是作为入口程序执行，就会执行 app.run()
if __name__ == '__main__':
    # 启动一个应用服务器，来接受用户的请求
    app.run()
