import os
from flask import Flask
from datetime import datetime

app = Flask(__name__)

"1"


@app.route("/rss/<path:file>")
def get_summary_rss(file):
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    BOOK_FILE = os.path.join(BASE_DIR, file)

    result = 0

    with open(BOOK_FILE) as book:
        lines = book.readlines()[1:]
        for i in range(len(lines)):
            line = lines[i].split()
            result += int(line[5])
        return str(result)


"2"
"get_mean_size.py"

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


STORAGE = {
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
    global STORAGE
    year, month, day = datetime.strptime(date, '%Y%m%d').year, \
        datetime.strptime(date, '%Y%m%d').month, \
        datetime.strptime(date, '%Y%m%d').day
    STORAGE.setdefault(int(date[:4]), {}).setdefault(int(date[4:6]), {}).setdefault(int(date[6:]), number)
    print(STORAGE)
    return f'Ваша дата{year, month, day} и сумма трат за этот день({number}) записаны!'


@app.route("/calculate/<int:year>")
def calculate_year(year: int):
    global STORAGE
    res = 0
    for i in STORAGE[year].values():
        for j in i.values():
            res += j
    return str(res)


@app.route("/calculate/<int:year>/<int:month>")
def calculate_month(year: int, month: int):
    global STORAGE
    m = STORAGE.get(year)
    d = m.get(month)
    res = sum(d.values())
    return str(res)


if __name__ == '__main__':
    app.run(debug=True)
