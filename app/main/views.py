from . import main
from flask import render_template,request,url_for,abort,redirect
from flask_login import login_required,current_user
from .forms import UpdateProfile,pitchForm,commentForm
from .. import db,photos
from ..models import  User, Pitch, Comment, Upvote, Downvote



@main.route('/')
def index():
    pitches = Pitch.query.all()
    health = Pitch.query.filter_by(category='health').all()
    comedy = Pitch.query.filter_by(category='comedy').all()
    business = Pitch.query.filter_by(category='business').all()

    return render_template('index.html',health=health,comedy=comedy,business=business,pitches=pitches)

@main.route('/new_pitch',methods=['GET', 'POST'])  
@login_required
def new_pitch():
    form = pitchForm()
    if form.validate_on_submit():
        title = form.title.data
        pitch = form.post.data
        category = form.category.data
        user_id = current_user._get_current_object().id
        new_pitch = Pitch(pitch=pitch,title =title ,category=category, user_id=user_id)
        new_pitch.save()
        return redirect(url_for('main.index'))
    return render_template('pitch.html', form=form)

@main.route('/user/<uname>') 
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)
    return render_template('profile/profile.html', user = user)


@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form =form) 

@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))



    