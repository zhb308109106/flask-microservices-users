# project/__init__.py
from flask import Flask, jsonify
import os
from flask_sqlalchemy import SQLAlchemy
#import sys
# 初始化app
app = Flask(__name__)
# 环境配置
#app.config.from_object('project.config.DevelopmentConfig')

# 初始化数据库
db = SQLAlchemy()
def create_app():
    # 初始化应用
    app = Flask(__name__)
    # 环境配置
    app_settings = os.getenv('APP_SETTINGS')
    app.config.from_object(app_settings)
    # 安装扩展
    db.init_app(app)
    # 注册blueprint
    from project.api.views import users_blueprint
    app.register_blueprint(users_blueprint)
    return app

