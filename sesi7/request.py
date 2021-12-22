from flask import Flask, request ,render_template
from markupsafe import escape

app = Flask(__name__)

@app.route('/user/<username>')
def show_user_profile(username):    
    # show the user profile for that user    
    return f'User {escape(username)}'

@app.route('/login', methods=['GET', 'POST'])
def login():    
    if request.method == 'POST':        
        return do_the_login()    
    else:        
        return show_the_login_form()
    
def do_the_login(): 
    return f'request method is {request.method}'

def show_the_login_form(): 
    return f'request method is {request.method}'
    

if __name__ == '__main__':
    app.run()