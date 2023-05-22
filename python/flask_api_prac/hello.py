from flask import Flask, jsonify
app = Flask(__name__)

count = 0

@app.route('/')
def hello_world():
    global count
    count += 1
    return jsonify(
        text="Hello, World!",
        count=count
        )
    
@app.route('/abuse')
def abuse_home():
    global count
    count += 100
    return jsonify(
        text="Welcom, Two",
        count=count
    )

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)