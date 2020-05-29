from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask import Blueprint
import sqlite3
import pandas as pd 
import os
import json
import jsonify 
import psycopg2
from psycopg2.extras import execute_values
import sqlite3
import numpy as np 
from flask import Flask 



#from web_app.routes.models import db, migrate, Game, parse_records
#from web_app.routes.gamehome_routes import gamehome_routes
#from web_app.routes.gameaddid_routes import gameaddid_routes

DATABASE_URI = "'trollsdb.sqlite3" # using relative filepath
#DATABASE_URI = "sqlite:////Users/Username/Desktop/your-repo-name/web_app_99.db" # using absolute filepath on Mac (recommended)
#DATABASE_URI = "sqlite:///C:\Users\JayBeast\Desktop\tweetme.db" # using absolute filepath on Windows (recommended) h/t: https://stackoverflow.com/a/19262231/670433

#db = SQLAlchemy()
#migrate = Migrate()
    
app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URI
#db.init_app(app)
#migrate.init_app(app, db)

#app.register_blueprint(hightroll_routes)
#app.register_blueprint(trollscore_routes)
#app.register_blueprint(usertext_routes)
#app.register_blueprint(home_routes)





#vaderroutes = Blueprint("vaderroutes_routes", __name__)
#trollscore_routes = Blueprint("trollscore_routes", __name__)
#usertext_routes = Blueprint("usertext_routes", __name__)
#hightroll_routes = Blueprint("hightroll_routes", __name__)
#home_routes = Blueprint("home_routes", __name__)

#class Troll(db.Model):
#    by = db.Column(db.String(128), primary_key=True)
#    text = db.Column(db.String(3000))
#    vader_score = db.Column(db.Integer, nullable=False)
#    neg_score = db.Column(db.Integer, nullable=False)

@app.route("/")
def about():
    return "Let's find some trolls!"

    
#@app.route("/hightroll/")
#def hightroll():
#    connection = sqlite3.connect("trollsdb.sqlite3")
#    cursor = connection.cursor()
#    hightroll = '''select distinct t.text, t.by, t.vader_score
#    from trolls_table as t where t.neg_score > .2 AND t.vader_score < -.7
#    order by t.neg_score DESC
#    limit 10;'''
#    r1 = cursor.execute(hightroll)
#    data =  (r1.fetchall())
#    df = pd.DataFrame(data, columns=[ 'text', 'username', 'score'])
#    result = df.to_json(orient='records')
#    
#    return result 

@app.route("/hightroll/")
def hightroll():
    connection = sqlite3.connect("trollsdb.sqlite3")
    cursor = connection.cursor()
    hightroll = '''select distinct(t.vader_score),  t.by, t.text
    from trolls_table as t
    where t.vader_score<-.85  and t.neg_score >.37 and length(t.text) <200
    order by t.vader_score
    limit 10;'''
    r1 = cursor.execute(hightroll)
    data =  (r1.fetchall())
    df = pd.DataFrame(data, columns=[ 'text', 'username', 'score'])
    result = df.to_json(orient='records')
    
    return result     

@app.route("/trollscore/<x>", methods=["GET","POST"])
def trollscore(x):
    connection = sqlite3.connect("trollsdb.sqlite3")
    cursor = connection.cursor()
    trollscore = f'''select t.by, avg(t.neg_score), avg(t.vader_score) from trolls_table as t  
    where t.by = '{x}';'''  
   
    r2 = cursor.execute(trollscore)
    data = (r2.fetchall())
    df = pd.DataFrame(data, columns=[ 'username', 'negativity','score'])

    result = df.to_json(orient='records')
    
    return result 

@app.route("/user/<x>", methods=["GET","POST"])
def usertext(x):
    connection = sqlite3.connect("trollsdb.sqlite3")
    cursor = connection.cursor()
    usertext = f'''select  distinct(t.text), t.by,  t.vader_score from trolls_table as t  
    where t.by = '{x}';'''
    r3 = cursor.execute(usertext)
    data = (r3.fetchall())
    df = pd.DataFrame(data, columns=[ 'text', 'username', 
                                     'score'])

    result = df.to_json(orient='records')
    
    return result 



    

#@user_text.route("/text")
#def user_text(x):
    #search through all texts, return all texts for user(x)  
#    db_user_text = text.query.filter_by(user='x')
#    return jsonify({all db_user_text})    
#cursor.neg_score.query.filter_by(by='x')              
        
 