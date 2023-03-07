import datetime
from flask import Flask
from random import choice

app = Flask(__name__)


@app.route('/hello_world')
def hello_world():
    return 'Привет, мир!'


CARS = ['Chevrolet', 'Renault', 'Ford', 'Lada']
@app.route('/cars')
def cars():
    return CARS


CATS = ['корниш-рекс', 'русская голубая', 'шотландская вислоухая', 'мейн-кун', 'манчкин']
@app.route('/cats')
def cats():
    return choice(CATS)


@app.route('/get_time/now')
def get_time_now():
    return 'Текущее время %s' % \
           datetime.datetime.now().utcnow()


@app.route('/get_time/future')
def get_time_future():
    return str(datetime.datetime.now() + datetime.timedelta(hours=1))


COUNTER = 0
@app.route('/counter')
def counter():
    global COUNTER
    COUNTER += 1
    return str(COUNTER)


if __name__ == '__main__':
    app.run(debug=True)
