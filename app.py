from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/greet", methods=["POST"])
def greet():
    name = request.form.get("name")

    message = f"Hello, {name}! Welcome to my website."

    return render_template("index.html", message=message)


if __name__ == "__main__":
    app.run(debug=True)

