from flask import Blueprint, render_template

user_routes = Blueprint('user_dashboard', __name__,
                        template_folder='templates')

route = 'user-dashboard'


@user_routes.route(f'/{route}/test')
def test_user():
    return 'user_dashboard'


@user_routes.route(f'/{route}/dashboard')
def user_dashboard():
    return render_template('user_dashboard/index.html')
