from flask import Flask,render_template

app = Flask(__name__)

@app.route('/hello/')
@app.route('/hello/<name>/<age>/')
def hello(name=None, age=None): 
    pets= ['cat','dog','bird','fish']
    pets_names = {'cat': 'neko','dog': 'inu','fish':'fsihi'}   
    return render_template('hello.html', name=name, age=age, pet_list=pets, len = len(pets))

if __name__ == '__main__':
    app.run()