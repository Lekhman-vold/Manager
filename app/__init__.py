import os
from flask import Flask, redirect, jsonify, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_security import Security, SQLAlchemyUserDatastore, auth_required
from flask_login import LoginManager
from dotenv import load_dotenv, dotenv_values

db = SQLAlchemy()
migrate = Migrate()
# config = dotenv_values(".env")
load_dotenv()


def create_app():
    from app.admin_dashboard import register_routes
    from app.admin_dashboard.controller import admin_routes
    from app.user_dashboard.controller import user_routes
    from app.login_page.controller import login_routes
    from app.models import register_models
    # from app.models.user import User, Role
    # global env

    app = Flask(__name__, template_folder='templates')

    @app.route('/')
    def redirect_to_login():
        return redirect('/login/')

    uri = os.getenv("DATABASE_URL")
    if uri.startswith("postgres://"):
        uri = uri.replace("postgres://", "postgresql://", 1)

    # CORS(app)
    app.config['SQLALCHEMY_DATABASE_URI'] = uri
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = os.getenv("SQLALCHEMY_TRACK_MODIFICATIONS")
    app.config['SECRET_KEY'] = os.getenv("SECRET_KEY")
    app.config['SECURITY_PASSWORD_SALT'] = 'MY_SALT'

    # global db_engine
    # db_engine = create_engine(env.DATABASE_URI)
    # user_datastore = SQLAlchemyUserDatastore(db, User, Role)
    # security = Security(app, user_datastore)

    db.init_app(app)

    login_manager = LoginManager()
    login_manager.login_view = 'login_page.login'
    login_manager.init_app(app)

    from app.models.user import User, Role

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(1)

    @app.errorhandler(500)
    def server_error(error):
        return jsonify({
            "success": False,
            "error": 500,
            "message": "server error!"
        }), 500

    app.register_blueprint(admin_routes)
    app.register_blueprint(user_routes)
    app.register_blueprint(login_routes)

    app.db = db

    migrate.init_app(app, db)

    register_models()
    register_routes()

    return app
