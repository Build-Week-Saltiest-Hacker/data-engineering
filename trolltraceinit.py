from flask import Flask

#from web_app.routes.models import db, migrate, Game, parse_records
#from web_app.routes.gamehome_routes import gamehome_routes
#from web_app.routes.gameaddid_routes import gameaddid_routes
from application.trolltrace import db, migrate, hightroll_routes, trollscore_routes, usertext_routes
DATABASE_URI = "'trollsdb.sqlite3" # using relative filepath
#DATABASE_URI = "sqlite:////Users/Username/Desktop/your-repo-name/web_app_99.db" # using absolute filepath on Mac (recommended)
#DATABASE_URI = "sqlite:///C:\Users\JayBeast\Desktop\tweetme.db" # using absolute filepath on Windows (recommended) h/t: https://stackoverflow.com/a/19262231/670433

def create_app():
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URI
    db.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(hightroll_routes)
    app.register_blueprint(trollscore_routes)
    app.register_blueprint(usertext_routes)

    return app

if __name__ == "__main__":
    my_app = create_app()
    my_app.run(debug=True)        