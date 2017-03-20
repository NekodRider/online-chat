from flask import render_template, flash, redirect,request,session,url_for,jsonify
from app import app,data


@app.route('/', methods=["POST", "GET"])
def message():
    content=data.getPost()
    if request.method == "POST":
        data.Post(request.get_data(as_text=True))
        content = data.getPost()
        return jsonify(content=content)
    else:
        return render_template("message.html",
                                title='Message',
                               content=content)