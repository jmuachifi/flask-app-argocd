from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('home.html', environment="Home")

@app.route("/dev")
def dev():
    return render_template('dev.html', environment="Development")

@app.route("/prod")
def prod():
    return render_template('prod.html', environment="Production")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
