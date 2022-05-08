from . import db



# id,username,password,email
# create user,save user, delete user

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255))


    def __repr__(self):
        return f'User {self.username}'