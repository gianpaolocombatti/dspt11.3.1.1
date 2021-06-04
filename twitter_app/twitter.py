from flask import Flask, request
from twitter_app.twitter_data_model import User, Tweet, DB
from twitter_app.twitter_database_functions import upsert_user

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///twitter_db.sqlite3'
DB.init_app(app)


@app.route('/')
def landing():
    twitter_handle = request.args['twitter_handle']
    new_user = upsert_user(twitter_handle)
    return '{}\'s tweets added to the database: {}'.format(new_user.name , ', '.join([t.text for t in new_user.tweets]))


if __name__ == '__main__':
    app.run()
