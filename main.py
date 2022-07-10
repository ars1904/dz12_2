from flask import Flask, render_template, request
from hh import parse

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/contact/')
def contact():
    return render_template('contact.html')

@app.route('/form/')
def form():
    return render_template('form.html')

@app.post('/form/')
def run_post():
    # Как получить данные формы
    text = request.form
    val= dict(text)['query_string']
    dat=parse(val)
    with open('main.txt', 'w') as f:
        f.write(f'{dict(text)}\n')
    return render_template('results.html', res=dat)

if __name__ == "__main__":
    app.run(host='127.0.0.9',port=4455,debug=True)