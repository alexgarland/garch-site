from flask import render_template, Flask, request
from stock_form import StockForm
from garch_calculation import return_garch

app = Flask(__name__)
app.config.from_object('config')


@app.route('/')
def hello_world():
    form = StockForm()
    return render_template('index.html', form = form)

@app.route('/', methods=["POST"])
def index_post():
    stock = request.form['stock']
    form = StockForm()
    results = return_garch(stock)
    rs = results.params
    return render_template('index_post.html', form=form, chosen=stock, model = rs)

if __name__ == '__main__':
    app.run()
