import sqlite3
import pandas as pd 
import os
import json
from dotenv import load_dotenv 
import psycopg2
from psycopg2.extras import execute_values
import sqlite3
import numpy as np 

connection = sqlite3.connect("trolldb.sqlite3")
cursor = connection.cursor()


def user_vader(meddlepal):
    connection = sqlite3.connect("trolldb.sqlite3")
    cursor = connection.cursor()
    uservader = '''select avg(t.neg_score), avg(t.vader_score) from troll_table as t  
    where t.by = 'meddlepal';'''
    r1 = cursor.execute(uservader)
    return ( r1.fetchall())

if __name__ == "__main__":
    print( r1.fetchall())    