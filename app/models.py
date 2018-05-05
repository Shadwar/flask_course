from datetime import datetime
from hashlib import md5
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from app import db, login


tags = db.Table(
    'posts_tags',
    db.Column('post_id', db.Integer, db.ForeignKey('post.id'), primary_key=True),
    db.Column('tag_id', db.Integer, db.ForeignKey('tag.id'), primary_key=True)
)

categories = db.Table(
    'posts_categories',
    db.Column('post_id', db.Integer, db.ForeignKey('post.id'), primary_key=True),
    db.Column('tag_id', db.Integer, db.ForeignKey('category.id'), primary_key=True)
)


@login.user_loader
def load_user(id):
    return User.query.get(int(id))


class User(UserMixin, db.Model):
    """ Пользователь """
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(128), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    posts = db.relationship('Post', backref='author', lazy='dynamic')
    about_me = db.Column(db.String(140))
    last_seen = db.Column(db.DateTime, default=datetime.utcnow)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def avatar(self, size):
        digest = md5(self.email.lower().encode('utf-8')).hexdigest()
        return 'https://www.gravatar.com/avatar/{}?d=identicon&s={}'.format(
            digest, size
        )

    def __repr__(self):
        return '<User {}>'.format(self.username)


class Post(db.Model):
    """ Пост - описание фильма """
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.Text)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    tags = db.relationship('Tag', secondary=tags, lazy='subquery',
                           backref=db.backref('posts', lazy=True))
    categories = db.relationship('Category', secondary=categories, lazy='subquery',
                           backref=db.backref('posts', lazy=True))

    def __repr__(self):
        return '<Post {}>'.format(self.body)


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(32), index=True, unique=True)
    slug = db.Column(db.String(32), index=True, unique=True)
    description = db.Column(db.Text)
    sort = db.Column(db.Integer)
    title_color = db.Column(db.String(7), default='#000000')
    title_background = db.Column(db.String(7), default='#897cd9')
    image = db.Column(db.String(128))

    def get_title_style(self):
        result = "color:{};".format(self.title_color) if self.title_color else ""
        result += "background-color:{};".format(self.title_background) if self.title_background else ""
        return result

    def __repr__(self):
        return '<Category {}>'.format(self.title)


class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(32), index=True, unique=True)
    slug = db.Column(db.String(32), index=True, unique=True)
    sort = db.Column(db.Integer)

    def __repr__(self):
        return '<Tag {}>'.format(self.title)
