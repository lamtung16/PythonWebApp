from flask import Blueprint, render_template, request

views = Blueprint(__name__, "views")

@views.route("/")
def home():
    args  = request.args
    _name = args.get('name')
    _age  = args.get('age')
    return render_template("index.html", name=_name, age=_age)