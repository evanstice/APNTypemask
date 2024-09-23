from zipapp import create_archive

from flask import Flask, render_template, request
from typemask import Typemask

app = Flask(__name__)
@app.route('/')
def index():
    return render_template('mainpage.html')
@app.route('/calculate.html', methods=['GET', 'POST'])
def calculate():
    carrier = request.form.get('option')
    typemask = Typemask(carrier)
    return render_template(
        'calculate.html', carrier = carrier
    )


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)