from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()

migrate = Migrate()

class Troll(db.Model):
    user = db.Column(db.String(128), primary_key=True)
    text = db.Column(db.String(3000))
    vader_score = db.Column(db.Integer, nullable=False)
    neg_score = db.Column(db.Integer, nullable=False)

    def high_troll(self):
        db_vader_score = text.query.filter_by(vader_score = max)
        return db_vader_score(0-10) 
        #find and return 10 texts where vader score is highest

    def user_vader(x):
        uservader = vader_score.query.filter_by(user='x')
        #find and return avg vader score for user x
        return uservader
         
    def user_neg(x):
        db_neg_score = neg_score.query.filter_by(user='x')
        #find and return avg neg_score for user x     
        return db_neg_score 

    def user_text(x):
        #search through all texts, return all texts for user(x)  
        db_user_text = text.query.filter_by(user='x')
        return all db_user_text    
              
        
          




    

