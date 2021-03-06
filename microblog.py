from app import app, db
from app.models import User, Post, Category, Tag, Slider, Slide

@app.shell_context_processor
def make_shell_context():
    return {
        'db': db,
        'User': User,
        'Post': Post,
        'Category': Category,
        'Tag': Tag,
        'Slider': Slider,
        'Slide': Slide
    }
