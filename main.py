"""
@author: raymondchen
@date: 2018/5/9
Description:
    This script is for the back end of the general project.
    Since the requirement is simple. I choose flask and mysql.
"""
from flask import jsonify, Flask, request, Response
from config import Config
from models import *
import time

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)


@app.route('/')
def hello_world():
    return 'hello world'


@app.route('/add')
def login():
    res = Response('add cookies')
    res.set_cookie(key='name', value='letian', expires=time.time()+6*60)
    return res


@app.route('/show')
def show():
    return request.cookies.__str__()


@app.route('/user', methods=['POST'])
@app.route('/user/<int:uid>')
def query_user(uid=None):
    if request.method == "POST":
        username = request.values.get("Username")
        if username is None:
            return jsonify({'error': "Parameters not found"}), "400 BAD REQUEST"
        m_user = User(uid=None, username=username)
        db.session.add(m_user)
        db.session.flush()
        print(m_user.uid)
        db.session.commit()
        return jsonify({'msg': "Sign up successfully."})
    m_user = User.query.filter_by(uid=uid).first()
    if m_user is None:
        return jsonify({'error': "User doesn't exist"}), "404 NOT FOUND"
    return jsonify(m_user.to_json())


@app.route('/addUsers')
def add_user():
    m_user = User(uid=None, username="testuser")
    db.session.add(m_user)
    db.session.commit()
    return "hello"


if __name__ == '__main__':
    app.run()
