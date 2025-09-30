
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>hello</h1>"

if __name__ == __name__:
    app.run(debug=True, host='127.0.0.1', port=5000)
    
    