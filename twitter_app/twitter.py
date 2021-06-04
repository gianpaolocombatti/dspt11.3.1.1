from flask import Flask, request
from twitter_app.twitter_data_model import User, Tweet, DB
import random

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///twitter_db.sqlite3'
DB.init_app(app)

@app.route('/')
def landing():
    user_name = request.args['user']
    new_user = User()
    new_user.id = random.randint(0, 9999999)
    new_user.name = user_name
    DB.session.add(new_user)
    DB.session.commit()
    return '{} added to the database'.format(user_name)


if __name__ == '__main__':
    app.run()