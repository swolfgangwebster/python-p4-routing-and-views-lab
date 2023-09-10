#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:param>')
def print_string(param):
    print(param)
    return f'<h1>{param}</h1>'

@app.route('/count/<int:param>')
def count(param):
    l = ''
    for i in range(param):
        l += f'{i}\n'
    
    return f'<pre>{l}</pre>'


@app.route('/math/<n1>/<op>/<n2>')
def math(n1, op, n2):
    n1 = int(n1)
    n2 = int(n2)
    if op == '+':
        return str(n1 + n2)
    if op == '-':
        return str(n1 - n2)
    if op == '*':
        return str(n1 * n2)
    if op == 'div':
        return str(n1/n2)
    if op == '%':
        return str(n1%n2)
    

if __name__ == '__main__':
    app.run(port=5555, debug=True)

