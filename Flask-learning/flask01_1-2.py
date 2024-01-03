from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index():
    # return render_template("index.html")
    return "Hello"


@app.route("/greet", methods=["POST", "GET"])
def greet():
    name = request.form["name"]
    greeting = f"hello, {name}"
    return greeting


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)