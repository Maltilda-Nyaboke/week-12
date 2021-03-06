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
    pass_secure = db.Column(db.String(255),nullable=False,unique=True)
    profile_pic_path = db.Column(db.String())
    pitches = db.relationship('Pitch',backref='user',lazy="dynamic")
    comments = db.relationship('Comment',backref='user',lazy="dynamic")
    upvotes = db.relationship('Upvote',backref='user',lazy="dynamic")
    downvotes = db.relationship('Downvote',backref='user',lazy="dynamic")

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
    title = db.Column(db.String,nullable=False)
    pitch = db.Column(db.String(255)) 
    category = db.Column(db.String,nullable=False)
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))
    comments = db.relationship('Comment',backref='pitch',lazy="dynamic")
    upvotes = db.relationship('Upvote',backref='pitch',lazy="dynamic")
    downvotes = db.relationship('Downvote',backref='pitch',lazy="dynamic")




    def save_pitch(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_pitches(cls,id):
        pitches = Pitch.query.filter_by(pitch_id=id).all()
        return pitches   

    

    def __repr__(self):
        return f'Pitch {self.pitch}'       




class Comment(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key=True)
    pitch_id = db.Column(db.Integer,db.ForeignKey("pitches.id"))
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))
    comment = db.Column(db.Text())



    def save_comment(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_comments(cls,id):
        comments = Comment.query.filter_by(pitch_id=id).all()
        return comments

    def __repr__(self):
        return f'Comment {self.comment}'       



class Upvote(db.Model): 
    __tablename__ = 'upvotes'
    id = db.Column(db.Integer, primary_key=True)
    upvote = db.Column(db.Integer,default=1)
    pitch_id = db.Column(db.Integer,db.ForeignKey("pitches.id"))
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))

    def save_upvote(self):
        db.session.add(self)
        db.session.commit()

    def delete_upvote(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def get_upvotes(cls,id):
        upvotes = Upvote.query.filter_by(pitch_id=id).all()
        return upvotes   


    def __repr__(self):
        return f'Upvote {self.votes}'       




class Downvote(db.Model):
    __tablename__ = 'downvotes' 
    id = db.Column(db.Integer, primary_key=True) 
    downvotes = db.Column(db.Integer,default=1)
    pitch_id = db.Column(db.Integer,db.ForeignKey("pitches.id"))
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))             

    def save_downvote(self):
        db.session.add(self)
        db.session.commit()

    def delete_downvote(self):
        db.session.delete(self)
        db.session.commit()


    @classmethod
    def get_downvotes(cls,id):
        downvotes = Upvote.query.filter_by(pitch_id=id).all()
        return downvotes   


    def __repr__(self):
        return f'Downvote {self.votes}'       
