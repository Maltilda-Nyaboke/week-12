from app import create_app,db
from flask import Flask
from flask_script import Manager,Server
from app.models import User,Pitch, Comment, Upvote, Downvote
from  flask_migrate import Migrate, MigrateCommand



app = create_app('development')


manager= Manager(app)
manager.add_command('server', Server)

@manager.shell
def make_shell_context():
    return dict(app = app,db = db,User = User,Pitch = Pitch,Comment= Comment, Upvote= Upvote, Downvote= Downvote )

migrate = Migrate(app,db)
manager.add_command('db',MigrateCommand)



if __name__ == '__main__':
    manager.run()