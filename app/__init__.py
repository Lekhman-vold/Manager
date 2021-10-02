from flask import Flask, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_security import Security, SQLAlchemyUserDatastore, auth_required
from flask_login import LoginManager

db = SQLAlchemy()
migrate = Migrate()


def create_app():
    from app.admin_dashboard import register_routes
    from app.admin_dashboard.controller import admin_routes
    from app.user_dashboard.controller import user_routes
    from app.login_page.controller import login_routes
    from app.models import register_models
    # from app.models.user import User, Role
    # global env

    app = Flask(__name__, template_folder='templates')

    # @app.before_first_request
    # def redirect_to_login():
    #     print("first")
    #     return redirect('/')

    # CORS(app)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://naruto:voloda2000@localhost:5432/lcg_manager'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    app.config['SECRET_KEY'] = 'pf9Wkove4IKEAXvy-cQkeDPhv9Cb3Ag-wyJILbq_dFw'
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

    app.register_blueprint(admin_routes)
    app.register_blueprint(user_routes)
    app.register_blueprint(login_routes)

    app.db = db

    migrate.init_app(app, db)

    register_models()
    register_routes()

    return app
