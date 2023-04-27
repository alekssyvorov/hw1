from flask import Flask, render_template, request
from random import randint

app = Flask(__name__)


@app.route('/')
def get_lst():
    return f'{constant}'


@app.route('/post')
def post_lst():
    constant.append(randint(-100, 100))
    return f'{constant}'


@app.route('/dell')
def dell_lst():
    constant.pop()
    return f'{constant}'


def create_lst():
    from random import randint
    for i in range(10):
        constant.append(randint(-50, 50))
    return constant


if __name__ == '__main__':
    constant = []
    constant = create_lst()
    app.run(host="0.0.0.0", port=10000, debug=True)