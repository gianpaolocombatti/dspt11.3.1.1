import psycopg2
import pandas as pd
import os
from data_model import DB

dbname = os.environ['PG_DB']
user = os.environ['PG_USER']
password = os.environ['PG_PASSWORD']
host = os.environ['PG_HOST']

conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host)
curs = conn.cursor()

select_characters_query = """select * from characters"""

curs.execute(select_characters_query)

results = curs.fetchall()

df = pd.DataFrame(results)

