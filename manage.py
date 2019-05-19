# manage.py


import unittest

import coverage

from flask.cli import FlaskGroup
from project.server.gunicornconfig import StandaloneApplication, options
from project.server import create_app, db
from project.server.models import User
from project.server.populate import populate_departements
from project.server.populate import populate_accidents
from project.server.populate import populate_lieux
from project.server.populate import populate_vehicules
from project.server.populate import populate_usagers
import subprocess
import sys

app = create_app()
cli = FlaskGroup(create_app=create_app)

# code coverage
COV = coverage.coverage(
    branch=True,
    include="project/*",
    omit=[
        "project/tests/*",
        "project/server/config.py",
        "project/server/*/__init__.py",
    ],
)
COV.start()


@cli.command()
def create_db():
    db.drop_all()
    db.create_all()
    db.session.commit()


@cli.command()
def drop_db():
    """Drops the db tables."""
    db.drop_all()


@cli.command()
def create_data():
    """Creates sample data."""
    print('LOADING DATA FILES ...')
    populate_departements()
    db.session.commit()
    populate_accidents()
    db.session.commit()
    populate_vehicules()
    db.session.commit()
    populate_usagers()
    db.session.commit()
    populate_lieux()
    db.session.commit()


@cli.command()
def test():
    """Runs the unit tests without test coverage."""
    tests = unittest.TestLoader().discover("project/tests", pattern="test*.py")
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        sys.exit(0)
    else:
        sys.exit(1)


@cli.command()
def cov():
    """Runs the unit tests with coverage."""
    tests = unittest.TestLoader().discover("project/tests")
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        COV.stop()
        COV.save()
        print("Coverage Summary:")
        COV.report()
        COV.html_report()
        COV.erase()
        sys.exit(0)
    else:
        sys.exit(1)

@cli.command()
def run_gunicorn():
    """Run with a production server"""
    StandaloneApplication(app, options).run()


@cli.command()
def flake():
    """Runs flake8 on the project."""
    subprocess.run(["flake8", "project"])


if __name__ == "__main__":
    cli()
