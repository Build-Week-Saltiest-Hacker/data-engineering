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
        db_text = text.query.all 
        db_vader_score = vader_score.query.all 
        #find and return 10 texts where vader score is highest

    def user_vader(x):
        db_user = user.query.all
        #find and return avg vader score for user x
         
    def user_neg(x):
        db_neg_score = neg_score.query.all
        #find and return avg neg_score for user x     
         
    def user_text(x):
        #search through all texts, return all texts for user(x)    
              
        
          




    

