from main import blog, db
from main.models import User, Post

@blog.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post}