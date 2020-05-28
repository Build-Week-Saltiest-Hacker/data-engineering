import sqlite3
import pandas as pd 
import os
import json
from dotenv import load_dotenv 
import psycopg2
from psycopg2.extras import execute_values
import sqlite3
import numpy as np 

connection = sqlite3.connect("trollsdb.sqlite3")
cursor = connection.cursor()


q1 = '''select t.text , t.by, t.neg_score, t.vader_score
from trolls_table as t 
order by t.vader_score DESC
limit 10;'''

r1 = cursor.execute(q1)

print( r1.fetchall())

q2 = ''' select t.by, t.neg_score, t.vader_score, t.text
from trolls_table as t 
where t.neg_score > .2 AND t.vader_score < -.6
order by t.neg_score DESC
limit 10;'''


r2= cursor.execute(q2)
print(r2.fetchall())

q3 = '''select avg(t.neg_score), avg(t.vader_score) from trolls_table as t  
where t.by = 'meddlepal';'''

r3 = cursor.execute(q3)
print(r3.fetchall())

q4 = '''select t.text   from trolls_table as t  
where t.by = 'meddlepal';'''
r4 = cursor.execute(q4)
print(r4.fetchall())


