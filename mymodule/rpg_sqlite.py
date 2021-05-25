import sqlite3
import pandas as pd

conn = sqlite3.connect('../rpg_db.sqlite3')

curs = conn.cursor()

select_weapon_query = """select *
from armory_weapon"""

select_item_query = """select *
from armory_item
"""

weapon_results = curs.execute(select_weapon_query).fetchall()

weapon_df = pd.DataFrame(weapon_results)

item_results = curs.execute(select_item_query).fetchall()

item_df = pd.DataFrame(item_results)

conn.close()

weapon_df.set_index(weapon_df.columns[0], inplace=True)
weapon_df.columns = ['power']

item_df.set_index(item_df.columns[0], inplace=True)
item_df.columns = ['name', 'value', 'weight']

item_df = item_df.join(weapon_df)

print(item_df.head())