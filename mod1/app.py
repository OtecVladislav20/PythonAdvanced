import datetime
from flask import Flask
from random import choice

app = Flask(__name__)


@app.route('/hello_world')
def hello_world():
    return 'Привет, мир!'


@app.route('/cars')
def cars():
    cars = ['Chevrolet', 'Renault', 'Ford', 'Lada']
    return cars


@app.route('/cats')
def cats():
    cats = ['корниш-рекс', 'русская голубая', 'шотландская вислоухая', 'мейн-кун', 'манчкин']
    return choice(cats)


@app.route('/get_time/now')
def get_time_now():
    return 'Текущее время %s' % \
           datetime.datetime.now().utcnow()


@app.route('/get_time/future')
def get_time_future():
    return str(datetime.datetime.now() + datetime.timedelta(hours=1))


if __name__ == '__main__':
    app.run(debug=True)
