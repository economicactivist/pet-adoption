from flask import Flask, request, render_template, redirect, flash, session, url_for
from flask.helpers import url_for
from flask_debugtoolbar import DebugToolbarExtension
from models import db, db_connect, Pet
from forms import AddPetForm

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///pet_adoption'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = "KJOJKLJKJLKJL"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
app.debug=True

debug = DebugToolbarExtension(app)

db_connect(app)
db.drop_all()
db.create_all()



@app.route('/')
def list_pets():
    pets = Pet.query.all()
    return render_template('pet-list.html', pets=pets)

@app.route('/add')
def add_pet():
    form = AddPetForm()
    return render_template('add-pet-form.html', form=form)

@app.route('/add', methods=['POST'])
def post_new_pet_to_db(form):
    
    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data or None
        age = form.age.data or None
        notes = form.notes.data or None
        available = form.available.data

        new_pet = Pet(name=name, species=species, photo_url=photo_url, age=age, notes=notes, available=available)

        db.session.add(new_pet)
        db.session.commit()
        flash(f'Added {name} to adoption list!')
        return redirect(url_for('list_pets'))
    else:
        return redirect(url_for('add_pet'))

@app.route('/<int:pet_id>')
def display_or_edit(pet_id):
    pet = Pet.query.get_or_404(pet_id)
    return render_template('display-or-edit.html', pet=pet)

# @app.route('/users/new')
# def add_new_user():
#     return render_template('new-user.html')

# @app.route('/users/new', methods=['POST'])
# def add_new_user_to_db():
#     first_name = request.form["first_name"]
#     last_name = request.form["last_name"]
#     image_url = request.form["img_url"] or None

#     new_user = User(first_name=first_name, last_name=last_name, image_url=image_url)
#     db.session.add(new_user)
#     db.session.commit()
#     #####################
#     return redirect(url_for('list_users'))

# @app.route('/users/<int:user_id>')
# def show_user_detail(user_id):
#     user = User.query.get_or_404(user_id)
#     posts = Post.query.filter_by(user_id=user_id)
#     print(user.image_url)
#     return render_template('user-detail.html', user=user, posts=posts)

# @app.route('/users/<int:user_id>/edit')
# def edit_user(user_id):
#     #maybe I should just pass user here

#     user = User.query.get_or_404(user_id)
#     return render_template('edit-user.html', user=user)

# @app.route('/users/<int:user_id>/edit', methods=['POST'])
# def post_user_edits_to_db(user_id):
#     user = User.query.get_or_404(user_id)
#     user.first_name = request.form["first_name"]
#     user.last_name = request.form["last_name"]
#     user.image_url = request.form["img_url"]
#     db.session.add(user)
#     db.session.commit()
#     return redirect(url_for('list_users'))

# @app.route('/users/<int:user_id>/delete')
# def delete_user(user_id):
#     flash('User Deleted')
#     user_id = int(user_id)
#     User.query.filter_by(id=user_id).delete()
#     return redirect(url_for('list_users'))

# @app.route('/users/<int:user_id>/posts/new')
# def create_post(user_id):
#     user = User.query.get_or_404(user_id)
#     tags = Tag.query.all()
#     return render_template('create-post.html', user=user, tags=tags)

# @app.route('/users/<int:user_id>/posts/new', methods=['POST'])
# def post_new_blog_post_to_db(user_id):
#     #!is this line necesary?
#     user = User.query.get_or_404(user_id)

#     post_title = request.form["post_title"]
#     post_content = request.form["post_content"]
#     tags = request.form.getlist('tag')
#     print()
#     print('********************')
#     print(tags)
#     print('********************')
#     print()
#     for tag in tags:
#         new_tag = Tag(name=tag)
#         db.session.add(new_tag)

#     #!not sure what to do next
#     new_post = Post(title=post_title, content=post_content, user_id=user.id)

#     db.session.add(new_post)
#     db.session.commit()
#     return redirect(url_for('show_user_detail', user_id = user.id))
#     #! why can't i just pass user_id directly?
#     #! Needs to be changed to post_id
#     #comment to update commit

# @app.route('/posts/<int:post_id>')
# def show_post(post_id):
#     post = Post.query.get_or_404(post_id)
#     return render_template('post-detail.html', post=post)

# @app.route('/posts/<int:post_id>/edit')
# def edit_post(post_id):
#     post = Post.query.get_or_404(post_id)
#     return render_template('edit-post.html', post=post)

# @app.route('/posts/<int:post_id>/edit', methods=['POST'])
# def post_blog_post_edits_to_db(post_id):
#     post = Post.query.get_or_404(post_id)
#     post.title = request.form["post_title"]
#     post.content = request.form["post_content"]
#     db.session.add(post)
#     db.session.commit()
#     return redirect(url_for('show_post', post_id=post.id))

# @app.route('/posts/<int:post_id>/delete')
# def delete_post(post_id):
#     flash('Post Deleted')
#     post_id = int(post_id)
#     post = Post.query.get_or_404(post_id)
#     Post.query.filter_by(id=post_id).delete()
#     db.session.commit()
#     return redirect(url_for('show_user_detail', user_id = post.user.id))

# @app.route('/tags')
# def list_tags():
#     tags = Tag.query.all()
#     return render_template('tags.html', tags=tags)

# @app.route('/tags/<int:tag_id>')
# def show_tag_detail(tag_id):
#     tag = Tag.query.get_or_404(tag_id)

#     # all posts matching a certain tag
#     # !tag_name = Tag.query.get_or_404(tag.name)  [remove later]


#     #get tag name for corresponding tag id
#     tagged_posts = tag.posts

#     return render_template('tag-detail.html', tag=tag, related_posts=tagged_posts)

# @app.route('/tags/new')
# def create_tag():
#     return render_template('create-tag.html')

# @app.route('/tags/new', methods=['POST'])
# def add_tag_to_db():
#     tag_name = request.form["tag_name"]
#     new_tag = Tag(name=tag_name)
#     db.session.add(new_tag)
#     db.session.commit()
#     return redirect(url_for('list_tags'))

# @app.route('/tags/<int:tag_id>/edit')
# def edit_tag(tag_id):
#     tag = Tag.query.get_or_404(tag_id)
#     return render_template('edit-tag.html', tag=tag)

# @app.route('/tags/<int:tag_id>/edit', methods=['POST'])
# def post_tag_edits_to_db(tag_id):
#     tag = Tag.query.get_or_404(tag_id)
#     tag.name = request.form["tag_name"]
#     db.session.add(tag)
#     db.session.commit()
#     return redirect(url_for('list_tags'))

# @app.route('/tags/<int:tag_id>/delete')
# def delete_tag(tag_id):
#     flash('Tag Deleted')
#     #! add message to html
#     Tag.query.filter_by(id=tag_id).delete()
#     db.session.commit()
#     return redirect(url_for('list_tags'))