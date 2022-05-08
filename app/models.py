from enum import unique
from . import db
from werkzeug.security import generate_password_hash,check_password_hash




# id,username,password,email
# create user,save user, delete user

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255),nullable=False,unique = True)
    email = db.Column(db.String(255),nullable=False,unique=True)
    pass_secure = db.Column(db.String(255),nullable=False)


    def save_user(self):
        db.session.add(self)
        db.session.commit()




    def __repr__(self):
        return f'User {self.username}'