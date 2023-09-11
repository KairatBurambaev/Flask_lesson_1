from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():

    return 'Приветствую тебя странник!'

@app.route('/Шляпа/')
@app.route('/шляпа/')

def hat():
    return 'Шляпа'

@app.route('/Мантия/')
@app.route('/мантия/')

def plash():
    return 'Мантия'

@app.route('/Посох/')
@app.route('/посох/')

def staff():
    return 'Посох'

if __name__ == '__main__':

    app.run(debug=True)