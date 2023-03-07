import os
from flask import Flask
from datetime import datetime

app = Flask(__name__)

"1"

@app.route("/rss/<path:file>")
def get_summary_rss(file):
    return 1


"2"

def get_mean_size():
    return 1


"3"
"decrypt.py"


"4"

@app.route("/hello-world/<string:name>")
def hello(name):
    day = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    weekday = datetime.today().weekday()
    return f"Hello, {name}. Have a good {day[weekday]}"


"5"

@app.route("/max_number/<path:number>")
def max_number(number):
    numbers = number.split("/")
    return f"Max number is <b>{max(numbers)}</b>"


"6"

@app.route("/preview/<int:size>/<path:file>")
def preview(size, file):
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    BOOK_FILE = os.path.join(BASE_DIR, file)

    with open(BOOK_FILE) as book:
        return book.read(size)


"7"
storage = {
    2000: {
        12: {
            1: 100,
            2: 100,
            3: 100
        },
        10: {
            1: 200,
            2: 100,
            3: 100
        }
    }
}

@app.route("/add/<date>/<int:number>")
def add(date: str, number: int):
    global storage
    year, month, day = datetime.strptime(date, '%Y%m%d').year, \
        datetime.strptime(date, '%Y%m%d').month, \
        datetime.strptime(date, '%Y%m%d').day
    if storage == {} or not storage.keys() in (str(year),):
        storage[year] = {month: {day: number}}
    elif not storage[year].keys() in (str(month),):
        storage[year][month] = {day: number}
    elif not storage[year][month].keys() in (str(day),):
        storage[year][month][day] = number
    print(storage)
    return f'Ваша дата{year, month, day} и сумма трат за этот день({number}) записаны!'


@app.route("/calculate/<int:year>")
def calculate_year(year: int):
    global storage
    res = 0
    m = storage.get(year)
    for k, v in m:
        d = k.get(v)
        res += d.values()
    return 1


@app.route("/calculate/<int:year>/<int:month>")
def calculate_month(year: int, month: int):
    global storage
    m = storage.get(year)
    d = m.get(month)
    res = sum(d.values())
    return str(res)


if __name__ == '__main__':
    app.run(debug=True)
