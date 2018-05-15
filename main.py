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


@app.route('/api/user', methods=['POST'])
@app.route('/api/user/<int:uid>')
def query_user(uid=None):
    if request.method == "POST":
        username = request.values.get("Username")
        if username is None:
            return jsonify({'error': "Parameters not found"}), "400 BAD REQUEST"
        m_user = User(uid=None, username=username)
        db.session.add(m_user)
        db.session.flush()
        res = jsonify({
            'msg': "Sign up successfully.",
            'content': {
                'UID': m_user.uid,
                'Username': m_user.username
            }
        })
        res.set_cookie(key="UID", value=str(m_user.uid), expires=9999999999)
        db.session.commit()
        return res
    m_user = User.query.filter_by(uid=uid).first()
    if m_user is None:
        return jsonify({'error': "User doesn't exist"}), "404 NOT FOUND"
    return jsonify(m_user.to_json())


@app.route('/api/score', methods=['POST'])
def record_score():
    game = request.values.get("Game", type=type(1))
    score = request.values.get("Score", type=type(1))
    if game is None or score is None:
        return jsonify({'error': "Parameters not found"}), "400 BAD REQUEST"
    uid = request.cookies.get("UID")
    m_user = User.query.filter_by(uid=uid).first()
    if m_user is None:
        return jsonify({"error": "You are unauthorized to make this request."}), "401 UNAUTHORIZED"
    if not record_score_for(game, score, uid):
        return jsonify({'error': "Parameters not found"}), "400 BAD REQUEST"
    return jsonify({"msg": "Record score successfully"})


def record_score_for(game, score, uid):
    if game == 1:
        m_score = Score1(uid=uid, score=score)
        db.session.add(m_score)
        db.session.commit()
    elif game == 2:
        m_score = Score2(uid=uid, score=score)
        db.session.add(m_score)
        db.session.commit()
    elif game == 3:
        m_score = Score3(uid=uid, score=score)
        db.session.add(m_score)
        db.session.commit()
    else:
        return False
    return True


if __name__ == '__main__':
    app.run()
