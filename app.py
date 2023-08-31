import flask
app = flask.Flask(__name__)

@app.route('/')
def hello():
    return "Hello, World!\nmain window"

@app.route('/square/<int:num>')
def square(num):
    result = num * num
    return f"The square of {num} is {result}"

@app.route('/hi/<string:name>')
def say_hi(name):
    return f"hi {name}, how you doing"

@app.route('/circle')
def circle_area():
    import json_data
    data = json_data.update_json_file(__file__[:-6] + "data.json")
    return "circle area calculated and stored in data.json === " + str(data)

app.run()