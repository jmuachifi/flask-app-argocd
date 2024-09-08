
from flask import Flask
import os

app = Flask(__name__)

@app.route("/dev")
def dev():
    return "This is the app instance in Dev enviroment!"

@app.route("/prod")
def test():
    return "This is the app instance in Prod enviroment!"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True,host='0.0.0.0',port=port)
