from flask import Flask
from markupsafe import escape
from flask import request

app = Flask(__name__)

# @app.route('/shop')
@app.route('/<page_name>')
def hello_world(page_name):
    html = 'Hello World, <br/> <h1> Hello World!</h1>'
    html += f'this is  page {page_name}'
    return html

@app.route("/<name>")
def hello(name):
    return f"Hello, {escape(name)}!"

@app.route('/user/<username>')
def show_user_profile(username):    
    # show the user profile for that user    
    return f'User {escape(username)}'

@app.route('/post/<int:post_id>')
def show_post(post_id):    
    # show the post with the given id, the id is an integer    
    return f'Post {post_id}'

@app.route('/path/<path:subpath>')
def show_subpath(subpath):    
    # show the subpath after /path/    
    return f'Subpath {escape(subpath)}'



if __name__ == '__main__':
    app.run()
