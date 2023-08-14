from flask import Flask
import json_data

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello, World!\nmain window"

@app.route('/square/<int:num>')
def square(num):
    result = num * num
    return f"The square of {num} is {result}"


@app.route('/circle')
def circle_area():
    json_data.update_json_file("data.json")
    return "circle area calculated and stored in data.json"


if __name__ == '__main__':
    app.run()