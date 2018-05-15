"""
@author: raymondchen
@date: 2018/5/11
Description:
"""
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    # 定义表名
    __tablename__ = 'User'
    # 定义列对象
    uid = db.Column(db.INT, primary_key=True)
    username = db.Column(db.VARCHAR(20))

    # repr()方法显示一个可读字符串，虽然不是完全必要，不过用于调试和测试还是很不错的。
    def __repr__(self):
        return '<User {}> '.format(self.uid, self.username)

    def to_json(self):
        return {
            'UID': self.uid,
            'Username': self.username
        }


class Score1(db.Model):
    # 定义表名
    __tablename__ = 'Score1'
    # 定义列对象
    uid = db.Column(db.INT, primary_key=True)
    score = db.Column(db.INT, primary_key=True)

    # repr()方法显示一个可读字符串，虽然不是完全必要，不过用于调试和测试还是很不错的。
    def __repr__(self):
        return '<User {}> '.format(self.uid, self.score)

    def to_json(self):
        return {
            'UID': self.uid,
            'Username': self.username
        }


class Score2(db.Model):
    # 定义表名
    __tablename__ = 'Score2'
    # 定义列对象
    uid = db.Column(db.INT, primary_key=True)
    score = db.Column(db.INT, primary_key=True)

    # repr()方法显示一个可读字符串，虽然不是完全必要，不过用于调试和测试还是很不错的。
    def __repr__(self):
        return '<User {}> '.format(self.uid, self.score)

    def to_json(self):
        return {
            'UID': self.uid,
            'Username': self.username
        }


class Score3(db.Model):
    # 定义表名
    __tablename__ = 'Score3'
    # 定义列对象
    uid = db.Column(db.INT, primary_key=True)
    score = db.Column(db.INT, primary_key=True)

    # repr()方法显示一个可读字符串，虽然不是完全必要，不过用于调试和测试还是很不错的。
    def __repr__(self):
        return '<User {}> '.format(self.uid, self.score)

    def to_json(self):
        return {
            'UID': self.uid,
            'Username': self.username
        }
