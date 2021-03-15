from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/test")
def test():
    return "to je test"

@app.route("/FAKEBOOK")
def FAKEBOOK():
    return render_template("FAKEBOOK.html")

@app.route("/FAKEBOOK")
def NEW_FAKEBOOK():
    return render_template("FAKEBOOK.html")

if __name__ == "__main__":
    app.run()