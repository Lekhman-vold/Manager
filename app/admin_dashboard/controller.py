from flask import Blueprint, render_template, request
from flask_security import current_user
from flask_login import login_required
from werkzeug.security import generate_password_hash

from app.models.user import User
from app import db
from datetime import datetime, timezone
import uuid
admin_routes = Blueprint('admin_dashboard', __name__,
                         template_folder='templates')

route = 'admin'


@admin_routes.route(f'/{route}/', methods=['get'])
def test():
    return 'admin_dashboard'


@admin_routes.route(f'/{route}/dashboard', methods=['get'])
@login_required
def dashboard():
    if current_user.is_authenticated:
        return render_template('examples/index.html', name=current_user.first_name)
    else:
        return "User is not auth"


@admin_routes.route(f'/{route}/user', methods=['get', 'post'])
@login_required
def user():
    if current_user.is_authenticated:
        if request.method == 'POST':
            email = request.form.get('email')
            first_name = request.form.get('first_name')
            last_name = request.form.get('last_name')
            department = request.form.get('department')
            country = request.form.get('country')
            birth_date = request.form.get('birth_date')
            password = 'pass'
            # create_user = User(email=email,
            #                    password='pass',
            #                    first_name=first_name,
            #                    last_name=last_name,
            #                    department=department,
            #                    county=country,
            #                    birth_date=datetime.now(tz=timezone.utc))
            create_user = User(email=email,
                               first_name=first_name,
                               last_name=last_name,
                               department=department,
                               county=country,
                               birth_date=datetime.now(tz=timezone.utc),
                               password=generate_password_hash(password, method='sha256'))
            print("User: ", create_user)
            db.session.add(create_user)
            db.session.commit()

        return render_template('examples/user.html')
    else:
        return render_template('error/index.html')


@admin_routes.route(f'/{route}/user-list', methods=['get', 'post'])
@login_required
def user_list():
    if current_user.is_authenticated:
        users = User.query
        return render_template('examples/tables.html', users=users)
    else:
        return render_template('error/index.html')


# @admin_routes.route(f'/{route}/create-user', methods=['post'])
# def create_user():
#     if request.method == 'POST':
#         print('ok')
#     return render_template('examples/user.html')
