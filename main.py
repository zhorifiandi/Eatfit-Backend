from app import app, db
from app.models import User, Post

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post}

#dummycommit
# git+https://github.com/nwcell/psycopg2-windows.git@win32-py34#egg=psycopg2
