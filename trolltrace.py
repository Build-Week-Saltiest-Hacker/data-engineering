from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask import Blueprint
import sqlite3
import pandas as pd 
import os
import json
from dotenv import load_dotenv 
import psycopg2
from psycopg2.extras import execute_values
import sqlite3
import numpy as np 



db = SQLAlchemy()
migrate = Migrate()

#vaderroutes = Blueprint("vaderroutes_routes", __name__)
trollscore_routes = Blueprint("trollscore_routes", __name__)
usertext_routes = Blueprint("usertext_routes", __name__)
hightroll_routes = Blueprint("hightroll_routes", __name__)

#class Troll(db.Model):
#    by = db.Column(db.String(128), primary_key=True)
#    text = db.Column(db.String(3000))
#    vader_score = db.Column(db.Integer, nullable=False)
#    neg_score = db.Column(db.Integer, nullable=False)


@hightroll_routes.route("/hightroll/")
def hightroll():
    connection = sqlite3.connect("trollsdb.sqlite3")
    cursor = connection.cursor()
    hightroll = '''select distinct t.text, t.by
    from trolls_table as t where t.neg_score > .2 AND t.vader_score < -.7
    order by t.neg_score DESC
    limit 10;'''
    r1 = cursor.execute(hightroll)
    return str( r1.fetchall())

@trollscore_routes.route("/trollscore/<x>")
def trollscore(x):
    connection = sqlite3.connect("trollsdb.sqlite3")
    cursor = connection.cursor()
    trollscore = f'''select avg(t.neg_score), avg(t.vader_score) from trolls_table as t  
    where t.by = '{x}';'''  
   
    r2 = cursor.execute(trollscore)
    return str(r2.fetchall())

@usertext_routes.route("/user/<x>")
def usertext(x):
    connection = sqlite3.connect("trollsdb.sqlite3")
    cursor = connection.cursor()
    usertext = f'''select t.text   from trolls_table as t  
    where t.by = '{x}';'''
    r3 = cursor.execute(usertext)
    return str(r3.fetchall())





    

#@user_text.route("/text")
#def user_text(x):
    #search through all texts, return all texts for user(x)  
#    db_user_text = text.query.filter_by(user='x')
#    return jsonify({all db_user_text})    
#cursor.neg_score.query.filter_by(by='x')              
        
          




    

