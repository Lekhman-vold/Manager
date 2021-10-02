from app import db
from flask_security import RoleMixin, UserMixin

roles_users = db.Table('roles_users',
                       db.Column('user_id', db.Integer(), db.ForeignKey('user.id')),
                       db.Column('role_id', db.Integer(), db.ForeignKey('role.id')))


class User(db.Model, UserMixin):
    __tablename__ = 'user'

    id = db.Column(db.Integer(), primary_key=True)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(500), nullable=False)
    is_active = db.Column(db.Boolean, default=True)
    first_name = db.Column(db.String(40), nullable=False)
    last_name = db.Column(db.String(40), nullable=False)
    department = db.Column(db.String(40), nullable=False)
    birth_date = db.Column(db.DateTime, nullable=True)
    county = db.Column(db.String(40), nullable=False)
    fs_uniquifier = db.Column(db.String(64), unique=True)
    roles = db.relationship('Role', secondary=roles_users,
                            backref=db.backref('users', lazy='dynamic'))


class Role(db.Model, RoleMixin):
    __tablename__ = 'role'

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(255))
