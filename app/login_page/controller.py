from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_user, login_required, logout_user
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime, timezone
from app import db
from app.models.user import User


login_routes = Blueprint('login_page', __name__,
                         template_folder='templates')


@login_routes.route('/login-test')
def test_login():
    return 'login_page'


@login_routes.route('/login/')
def login():
    return render_template('login/index.html')


@login_routes.route('/login/', methods=['post'])
def login_dashboard():
    email = request.form.get('email')
    password = request.form.get('password')
    print(email, password)

    user = User.query.filter_by(email=email).first()

    if not user or not check_password_hash(user.password, password):
        flash('Please check your login details and try again.')
        return redirect(url_for('login_page.login'))

    login_user(user)
    print(user)
    return redirect(url_for('admin_dashboard.dashboard'))


@login_routes.route('/logout/')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login_page.login'))


@login_routes.route('/forgot')
def create_test_user():
    create_user = User(email='volodymyr@yahoo.com',
                       first_name='admin',
                       last_name='admin',
                       department='programmer',
                       county='test',
                       birth_date=datetime.now(tz=timezone.utc),
                       password=generate_password_hash('pass', method='sha256'))
    print("User: ", create_user)
    db.session.add(create_user)
    db.session.commit()
    return "Create"
