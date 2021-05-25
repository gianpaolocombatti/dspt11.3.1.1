import pymongo
import sqlite3
import os

mongo_pass = os.environ['MONGO_PASS']

mongo_client = pymongo.MongoClient(
    "mongodb://localhost/myFirstDatabase?retryWrites=true&w=majority".format(mongo_pass))

sqlite_conn = sqlite3.connect(os.path.abspath(os.path.join(os.path.dirname(__file__), "../rpg_db.sqlite3")))
sqlite_cursor = sqlite_conn.cursor()
db = mongo_client.myFirstDatabase
if not 'rpg_data' in db.list_collection_names():
    db.create_collection('rpg_data')

character_query = """SELECT * FROM charactercreator_character;"""

item_query = """SELECT * FROM armory_item left armory_weapon on armory_item.item_id = armory_weapon.item_ptr_id;"""


character_results = sqlite_cursor.execute(character_query).fetchall()

for c in character_results:
    doc = {}
    keys = [col[0] for col in sqlite_cursor.description]
    for i, key in enumerate(keys):
        doc.update({key: c[i]})
    print(doc)
    db.rpg_data.insert_one(doc)



#query from sql lite and insert into mongo.