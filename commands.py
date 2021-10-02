import click
from flask.cli import with_appcontext

from app import db
from app.models.user import User, Role


@click.command(name='create_tables')
@with_appcontext
def create_tables():
    db.create_all()

create_tables()
