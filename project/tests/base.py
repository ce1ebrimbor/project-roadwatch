# project/server/tests/base.py


from flask_testing import TestCase
from project.server import db, create_app
from project.server.models import User
import jwt
import datetime

app = create_app()


class BaseTestCase(TestCase):
    def create_app(self):
        app.config.from_object("project.server.config.TestingConfig")
        # create a dummy user
        user_mail = "dummyuser@dummymail.com"
        user = User.query.filter_by(email=user_mail).first()

        if user is None:
        	user = User(email=user_mail)
        	user.set_password("dummy")
        	db.session.add(user)
        	db.session.commit()
        	user = User.query.filter_by(email=user_mail).first()

        user_id = user.get_id()

        self.token = jwt.encode({'id': user_id,
                       'exp': datetime.datetime.utcnow() + datetime.timedelta(days=365)},
                        app.config['SECRET_KEY'])
        return app

    def tearDown(self):
        db.session.remove()
