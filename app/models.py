from enum import unique
from . import db
from . import login_manager
from flask_login import UserMixin
from werkzeug.security import generate_password_hash,check_password_hash




# id,username,password,email
# create user,save user, delete user

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(UserMixin,db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255),nullable=False,unique = True)
    email = db.Column(db.String(255),nullable=False,unique=True)
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    pass_secure = db.Column(db.String(255),nullable=False)

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self,password):
        self.pass_secure = generate_password_hash(password) 

    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)      


    def save_user(self):
        db.session.add(self)
        db.session.commit()

    def delete_user(self):
        db.session.delete(self)
        db.session.commit()    




    def __repr__(self):
        return f'User {self.username}'

class Pitch(db.Model):
    __tablename__ = 'pitches'  
    id = db.Column(db.Integer, primary_key=True) 



class Comment(db.Model):
    __tablename__ = 'comments'






class Upvote(db.Model): 
    __tablename__ = 'upvotes'





class Downvote(db.Model):
    __tablename__ = 'downvotes'               