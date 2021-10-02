from flask import Blueprint

user_routes = Blueprint('user_dashboard', __name__,
                        template_folder='templates')


@user_routes.route('/user')
def test_user():
    return 'user_dashboard'

