import sqlite3
import os
import csv
import pandas as pd 
import json
from dotenv import load_dotenv 
import psycopg2
from psycopg2.extras import execute_values



CSV_FILEPATH = os.path.join(os.path.dirname(__file__), "hackernews5.csv")
df = pd.read_csv(CSV_FILEPATH)
print(df.head())

# creates the actual sqlite file, even if it doesnt exist, then it converts csv to DB in sqlite
conn = sqlite3.connect('trollsdb.sqlite3')

df.to_sql('trolls_table', conn, if_exists='append', index=False)


