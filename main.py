from typemask import Typemask
from flask import Flask

app = Flask(__name__)
@app.route('/')
def index() -> object:
    return 'TESTING out Flask'

if __name__ == '__main__':
    app.run()