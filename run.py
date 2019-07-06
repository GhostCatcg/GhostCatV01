#!/usr/bin/python
# -*- coding:UTF-8 -*-

from flask import Flask, request, render_template, redirect, url_for, jsonify
from DB import *
import time
import json

app = Flask(__name__)

app.jinja_env.variable_start_string = '{{{ '
app.jinja_env.variable_end_string = ' }}}'



@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template("index.html")



@app.route("/message", methods=["GET", "POST"])
def message():
    usermessage = {}

    if request.method == "GET":
        return json.dumps(readDB(), ensure_ascii=False)
    else:
        name = (request.form["name"])
        email = (request.form["email"])
        wechat = (request.form["wechat"])
        website = (request.form["website"])
        content = (request.form["content"])
        nowtime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        filename = time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime())

        usermessage.update({"name": name,
                            "email": email,
                            "wechat": wechat,
                            "website": website,
                            "content": content,
                            "time": nowtime})
        writeDB(usermessage, filename)
        # print(usermessage)
        return jsonify({'msg': '成功', 'code': 1, 'data': usermessage})


@app.route("/admin", methods=["GET", "POST"])
def admin():

    if request.method == "GET":
        return render_template("admin.html")
    else:
        id = request.form["id"]
        delDB(id)
        return render_template("admin.html")


# 抛出404错误
@app.errorhandler(404)
def not_fonud(e):
    return "页面没找到哦..."
    # return render_template("404.html")

# 主动抛出异常
# abort(404)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=9000, debug=True)