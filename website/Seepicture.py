from flask import Flask, render_template, request, flash, redirect, url_for
from flask import g
from flask_bootstrap import Bootstrap


app = Flask(__name__)
app.config["SECRET_KEY"] = "secret key"
bootstrap = Bootstrap(app)


# 服务器初始化
@app.before_first_request
def server_init():
    print("Server init.")
    #setattr(g, "info", "abc177")


# 请求之前的钩子
@app.before_request
def before_request():
    pass


# 主页
@app.route("/")
def index():
    return render_template("index.html")


# 搜索页面
@app.route("/query_result", methods=["post"])
def query_result():
    keyword = request.form["keyword"]
    print("Query Keyword: " + keyword)
    # TODO
    return render_template("query_result.html")


# 错误页面
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404


# 服务器内部错误
@app.errorhandler(500)
def internal_error(e):
    return render_template("500.html"), 500


if __name__ == "__main__":
    app.run("0.0.0.0", 80, True)
