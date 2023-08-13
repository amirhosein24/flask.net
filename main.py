from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, this is your Flask web application!'
#its being shows in web screen
# http://127.0.0.1:5000

@app.route('/api/data', methods=['POST'])
def process_data():
    data = request.get_json()
    # Process the data as needed
    # You can also make requests to the .NET API here
    return 'Data processed successfully'

if __name__ == '__main__':
    app.run()