from flask import Flask, render_template, request, g, flash, redirect, url_for, make_response
from flask_bootstrap import Bootstrap
import Store


app = Flask(__name__)
boostrap = Bootstrap(app)
app.config["SECRET_KEY"] = "secret key"
store = None


# 服务器初始化
@app.before_first_request
def server_init():
    print("Server init.")
    global store
    store = Store.Store("127.0.0.1", 27017, "t66y_pic")


# 请求之前的钩子
@app.before_request
def before_request():
    pass


# 主页
@app.route("/")
def index():
    return render_template("index.html")


# 搜索页面
@app.route("/query_result", methods=["POST"])
def query_result():
    keyword = request.form["keyword"]

    print("Query Keyword: " + keyword)

    global store
    res = store.get_threads_by_keyword(keyword)

    return render_template("query_result.html", thread_info=res, cur_keyword=keyword)


# 套图页面
@app.route("/pic_result", methods=["POST"])
def pic_result():
    tid = request.form["tid"]

    global store
    image_urls = store.get_images_by_tid(tid)
    thread_name = store.get_thread_name(tid)

    print("Request Thread: " + thread_name)

    return render_template("pic_result.html", name=thread_name, images=image_urls)


# 获取图片
@app.route("/get_picture", methods=["GET"])
def get_picture():
    url = request.args['url']

    print("Get picrure: " + url)

    global store
    response = make_response(store.get_image_data_by_url(url))

    ext_name = url.split(".")[-1]
    response.headers["Content-type"] = "image/" + ext_name

    return response


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
