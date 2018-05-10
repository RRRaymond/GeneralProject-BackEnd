"""
@author: raymondchen
@date: 2018/5/9
Description:
    This script is for the back end of the general project.
    Since the requirement is simple. I choose flask and mysql.
"""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)


class User(db.Model):
    # 定义表名
    __tablename__ = 'User'
    # 定义列对象
    uid = db.Column(db.INT, primary_key=True)
    username = db.Column(db.VARCHAR(20))
    # repr()方法显示一个可读字符串，虽然不是完全必要，不过用于调试和测试还是很不错的。
    def __repr__(self):
        return '<User {}> '.format(self.uid)


@app.route('/')
def hello_world():
    return 'Hello Flask!'


@app.route('/Users')
def query_user():
    a = User.query.all()
    b = a[0].uid
    return a


@app.route('/addUsers')
def add_user():
    m_user = User(uid=None, username="testuser")
    db.session.add(m_user)
    db.session.commit()
    return "hello"


if __name__ == '__main__':
    db.init_app(app)
    app.run()