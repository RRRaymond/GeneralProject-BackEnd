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
    return 'hello world'


@app.route('/api/user', methods=['POST', 'GET'])
def query_user():
    if request.method == "POST":
        username = request.values.get("Username")
        if username is None:
            return jsonify({'error': "Parameters not found"}), "400 BAD REQUEST"
        m_user = User(uid=None, username=username)
        db.session.add(m_user)
        db.session.flush()
        db.session.add(Score1(uid=m_user.uid, score=0))
        db.session.add(Score2(uid=m_user.uid, score=0))
        db.session.add(Score3(uid=m_user.uid, score=0))
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
    uid = request.cookies.get("UID")
    if uid is None:
        return jsonify({"error": "You are unauthorized to make this request."}), "401 UNAUTHORIZED"
    m_user = User.query.filter_by(uid=uid).first()
    if m_user is None:
        return jsonify({'error': "User doesn't exist"}), "404 NOT FOUND"
    m_user_json = m_user.to_json()
    scores = query_score(uid)
    m_user_json["score"] = {
        "Game1": scores[0] if scores[0] is not None else 0,
        "Game2": scores[1] if scores[1] is not None else 0,
        "Game3": scores[2] if scores[2] is not None else 0
    }
    return jsonify(m_user_json)


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


@app.route('/api/score/<path:game>', methods=['GET'])
def leaderboard(game):
    games = ['game1', 'game2', 'game3']
    if game not in games:
        return jsonify({'error': "Parameters not found"}), "400 BAD REQUEST"
    LeaderBoards = [LeaderBoard1, LeaderBoard2, LeaderBoard3]
    leaders = LeaderBoards[games.index(game)].query.all()
    temp = []
    for i in range(len(leaders)):
        temp.append(leaders[i].to_json())
    res = {
        "Game": game,
        "Count": len(leaders),
        "Content": temp
    }
    return jsonify(res)


def record_score_for(game, score, uid):
    if game not in [1, 2, 3]:
        return False
    Scores = [Score1, Score2, Score3]
    m_score = Scores[game-1].query.filter_by(uid=uid).first()
    if m_score is None:
        m_score = Scores[game-1](uid=uid, score=score)
        db.session.add(m_score)
    else:
        m_score.score = score if score > m_score.score else m_score
    db.session.commit()
    return True


def query_score(uid):
    m_score1 = Score1.query.filter_by(uid=uid).with_entities(db.func.max(Score1.score)).scalar()
    m_score2 = Score2.query.filter_by(uid=uid).with_entities(db.func.max(Score2.score)).scalar()
    m_score3 = Score3.query.filter_by(uid=uid).with_entities(db.func.max(Score3.score)).scalar()
    return m_score1, m_score2, m_score3


if __name__ == '__main__':
    app.run(host="0.0.0.0")
