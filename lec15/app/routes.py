from datetime import datetime

from flask import flash, redirect, render_template, request, url_for
from flask_login import current_user, login_required, login_user, logout_user
from werkzeug.urls import url_parse

from app import app, db
from app.forms import LoginForm, RegistrationForm, EditUserInfoForm
from app.models import User


@app.before_request
def before_request():
    if current_user.is_authenticated:
        current_user.last_seen = datetime.utcnow()
        db.session.commit()

mock_posts = [
    {
        'author' : {"username" : "Bob"},
        'body' : "It's my first post on this site!",
    },
    {
        'author' : {"username" : "Alice"},
        'body' : "Cool!",
    },
    {
        'author' : {"username" : "Alex"},
        'body' : "My fav book is LOTR!",
    },
]

@app.route('/', methods=['GET'])
@app.route('/home', methods=['GET'])
@login_required
def home():
    return render_template('home.html', title= 'Home', posts=mock_posts)


@app.route('/about', methods=['GET'])
@login_required
def about():
    return render_template('about.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password2.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('login'))

    return render_template('register.html', form=form )


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username = form.username.data).first()
        if user is None:
            flash('Invalid username. Try login again')
            return redirect(url_for('login'))
        elif not user.check_password(form.password.data):
            flash('Invalid password. Try login again')
            return redirect(url_for('login'))
        else:
            login_user(user, remember=form.remember_me.data)
            next_page = request.args.get('next')
            if not next_page or url_parse(next_page).netloc != '':
                next_page = url_for('about')
            return redirect(next_page)

    return render_template('login.html', form=form )


@app.route('/logout', methods=['GET'])
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route('/user/<username>', methods=['GET'])
@login_required
def user(username):
    # store = Store.query.filter_by(inn = store_inn).first_or_404()
    # books = Book.query.filter_by(store_id = store.id)
    # books.sort(key=lambda x: x.bookname)
    # return render_template(.....)
    user = User.query.filter_by(username=username).first_or_404()
    posts = [
        {'author' : user, 'body': 'Test body 1'},
        {'author' : user, 'body': 'Test body 2'},
        {'author' : user, 'body': 'Test body 3'},
        {'author' : user, 'body': 'Test body 4'},
    ]

    return render_template('user.html', user=user, posts=posts)


@app.route('/edit', methods=['GET', 'POST'])
@login_required
def edit():
    form = EditUserInfoForm(current_user.username)
    if form.validate_on_submit():
        current_user.username = form.username.data 
        current_user.about_me = form.about_me.data 
        db.session.commit()

        return redirect(url_for('home'))
    elif request.method == 'GET':
        form.username.data = current_user.username 
        form.about_me.data = current_user.about_me
    return render_template('edit_user.html', form=form)


@app.route('/follow/<username>', methods=['GET'])
@login_required
def follow(username):
    user = User.query.filter_by(username=username).first()
    if user is None:
        flash('User {} not found'.format(username))
        return redirect(url_for('home'))
    if user == current_user:
        flash("You can not follow yourself")
        return redirect(url_for('user', username=username))
    current_user.follow(user)
    db.session.commit()
    flash('You are following {}'.format(username))
    return redirect(url_for('user', username=username))


@app.route('/unfollow/<username>', methods=['GET'])
@login_required
def unfollow(username):
    user = User.query.filter_by(username=username)
    # add check to ungollowing
    if user is None:
        flash('User {} not found'.format(username))
        return redirect(url_for('home'))
    if user == current_user:
        flash("You can not unfollow yourself")
        return redirect(url_for('user', username=username))

    current_user.unfollow(user)
    db.session.commit()
    flash('You are unfollowing {}'.format(username))
    return redirect(url_for('user', username=username))


    



# @app.route('/store/<store_inn>', methods=['GET'])
# def store(store_inn):
#     store = Store.query.filter_by(inn = store_inn).first_or_404()
#     books = Book.query.filter_by(store_id = store.id)
#     if len(books) == 0:
#         books = None
#     else: 
#         books.sort(key=lambda x: x.bookname)
#     return render_template('store_info.html', books=books, store=store)

