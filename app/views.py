from flask import render_template, flash, redirect,request,session,url_for,jsonify
from app import app,data
@app.route('/',methods=["POST","GET"])
def message():
    content=data.getPost()
    if request.method == "POST" and request.headers.has_key("X-Requested-With"):
        new_content = request.form.get("content", "null")
        data.Post(new_content)
        content = data.getPost()
        return jsonify(content=content)
        #return render_template("message.html",
        #                          title='Message',
        #                          content=content)
    elif request.method == "POST":
        new_content = request.form.get("content", "null")
        data.Post(new_content)
        content = data.getPost()
        return jsonify(content=content)
        #return render_template("message.html",
        #                          title='Message',
        #                          content=content)
    else:
        return render_template("message.html",
                                title='Message',
                               content=content)
