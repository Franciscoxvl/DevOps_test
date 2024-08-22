from flask import Flask, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, World!"

@app.route('/main')
def main():
    return render_template("index.html")

@app.route('/status')
def status():
    return jsonify({"status": "running"})

@app.route('/about')
def about():
    return jsonify({"message": "This is a sample Flask application"})

if __name__ == '__main__':
    app.run()
