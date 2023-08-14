from flask import Flask

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
    import json_data
    import time

    json_data.update_json_file("data.json")
    time.sleep(3)
    return "circle area calculated and stored in data.json"


if __name__ == '__main__':
    app.run()