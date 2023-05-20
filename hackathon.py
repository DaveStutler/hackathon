from flask import Flask

app = Flask(__name__)

@app.route('/api/example', methods=['GET'])
def example_endpoint():
    return 'Hello, world. This is the example endpoint.'

if __name__ == '__main__':
    app.run()