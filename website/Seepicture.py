from flask import Flask
from flask import render_template
from flask import request
from flask_bootstrap import Bootstrap


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


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404


if __name__ == "__main__":
    bootstrap = Bootstrap(app)
    app.run("0.0.0.0", 80, True)
