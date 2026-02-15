from flask import render_template, redirect, url_for, flash, request, abort
from flask_login import login_user, current_user, logout_user, login_required
from urllib.parse import urlparse, urljoin
from resolution import app, db, bcrypt
from resolution.forms import RegistrationForm, LoginForm, CreatePostFrProfileForm, PostForm
from resolution.models import User, Post



@app.route('/')
def home():
	posts = Post.query.all()
	return render_template('home.html', posts=posts)


@app.route('/post/<int:post_id>')
def detail(post_id):
	post = Post.query.get_or_404(post_id)
	return render_template('detail.html', post=post)


@app.route('/register', methods=['GET', 'POST'])
def register():
	form = RegistrationForm()
	if form.validate_on_submit():
		hashed_pass = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
		user = User(username=form.username.data, email=form.email.data, password=hashed_pass)
		db.session.add(user)
		db.session.commit()
		flash('Registration done!', 'success')
		return redirect(url_for('home'))
	return render_template('register.html', form=form)


def is_safe_url(target):
    ref_url = urlparse(request.host_url)
    test_url = urlparse(urljoin(request.host_url, target))
    return test_url.scheme in ('http', 'https') and \
           ref_url.netloc == test_url.netloc

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user)
            
            next_page = request.args.get('next')
            
            if not next_page or not is_safe_url(next_page):
                next_page = url_for('home')
            
            flash('Logging in done!', 'success')
            return redirect(next_page)
        else:
            flash('Email or Password is wrong', 'danger')
            
    return render_template('login.html', form=form)



@app.route('/logout')
@login_required
def logout():
	logout_user()
	flash('logging out done!', 'success')
	return redirect(url_for('home'))


@app.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
	form = CreatePostFrProfileForm()
	if request.method == 'GET':
		form.username.data = current_user.username
		form.email.data = current_user.email
	return render_template('profile.html', form=form)


@app.route('/post/new', methods=['GET', 'POST'])
@login_required
def new_post():
	form = PostForm()
	if form.validate_on_submit():
		post = Post(title=form.title.data, content=form.content.data, author=current_user)
		db.session.add(post)
		db.session.commit()
		flash('Post created', 'info')
		return redirect(url_for('home'))
	return render_template('create_post.html', form=form)


@app.route('/post/<int:post_id>/delete')
@login_required
def delete(post_id):
	post = Post.query.get_or_404(post_id)
	if post.author != current_user:
		abort(403)
	db.session.delete(post)
	db.session.commit()
	flash('Post deleted', 'info')
	return redirect(url_for('home'))

@app.route("/post/<int:post_id>/update", methods=['GET', 'POST'])
@login_required
def update_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    
    form = PostForm() 
    
    if form.validate_on_submit():
        post.title = form.title.data
        post.content = form.content.data
        db.session.commit()
        flash('Your resolution has been updated!', 'success')
        return redirect(url_for('home'))
    elif request.method == 'GET':
        form.title.data = post.title
        form.content.data = post.content
        
    return render_template('create_post.html', title='Update Resolution', form=form)







