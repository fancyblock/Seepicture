from flask import Flask, render_template, request, g, flash, redirect, url_for
import Store


app = Flask(__name__)
app.config["SECRET_KEY"] = "secret key"
store = None


# 服务器初始化
@app.before_first_request
def server_init():
    print("Server init.")
    global store
    store = Store.Store("127.0.0.1", 27017, "milf_pic")


# 请求之前的钩子
@app.before_request
def before_request():
    pass


# 登录页面
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # TODO
        flash("登录成功")
        return redirect(url_for("index"))
    else:
        return render_template("login.html")


# 主页
@app.route("/")
def index():
    return render_template("index.html")


# 搜索页面
@app.route("/query_result", methods=["POST"])
def query_result():
    keyword = request.form["keyword"]
    page_index = 0
    if "pageIndex" in request.form:
        page_index = request.form["pageIndex"]

    print("Query Keyword: " + keyword + " , page " + str(page_index))

    global store
    res = store.get_threads_by_keyword(keyword)

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
