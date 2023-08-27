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
    json_data.update_json_file("data.json")
    return "circle area calculated and stored in data.json" 


@app.route('/hi/<string:name>')
def hi(name):
    return f"hi {name}, how are you doing today ?"

app.run()