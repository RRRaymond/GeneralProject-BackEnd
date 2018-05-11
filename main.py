"""
@author: raymondchen
@date: 2018/5/9
Description:
    This script is for the back end of the general project.
    Since the requirement is simple. I choose flask and mysql.
"""
from flask import jsonify, Flask, request
from config import Config
from models import *

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)


@app.route('/')
def hello_world():
    return 'Hello Flask!'


@app.route('/user/', methods=['POST'])
@app.route('/user/<int:uid>')
def query_user(uid=None):
    if request.method == "POST":
        return "TODO"
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
