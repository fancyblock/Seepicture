from flask import Flask
from flask import render_template
from flask import request


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/query_result", methods=["post"])
def query_result():
    keyword = request.form["keyword"]
    print("Query Keyword: " + keyword)
    #TODO
    return render_template("query_result.html")


if __name__ == "__main__":
    app.run("0.0.0.0", 80, True)
