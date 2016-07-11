from flask import render_template, Flask
from app import app
from .forms import StockForm

app = Flask(__name__)


@app.route('/')
def hello_world():
    form = StockForm()
    return render_template('index.html', form = form)


if __name__ == '__main__':
    app.run()
