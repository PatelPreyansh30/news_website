from flask import render_template, redirect, request, flash
from base import app
from base.com.vo import UserVO
from base.com.dao import UserDAO


@app.route("/", methods=['GET'])
def home():
    return render_template('home.html', show_navigation=True)


@app.route("/contact-us", methods=['GET'])
def contact_us():
    return render_template('contact.html', show_navigation=True)


@app.route("/news", methods=['GET'])
def news():
    return render_template("news.html", show_navigation=True)


@app.route("/add-news", methods=['GET', 'POST'])
def add_news():
    if request.method == 'GET':
        return render_template("add_news.html", show_navigation=True)
    elif request.method == 'POST':
        pass


@app.route("/register", methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    elif request.method == 'POST':
        user_vo = UserVO()
        user_dao = UserDAO()
        if user_dao.get_user(request.form.get('username')):
            flash("Username already exists")
        else:
            user_vo.first_name = request.form.get('firstname')
            user_vo.last_name = request.form.get('lastname')
            user_vo.email = request.form.get('username')
            user_vo.password = request.form.get('password')
            user_dao.insert(user_vo)
            flash("User register successfully.")
        return redirect("/register")


@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template("login.html")
    elif request.method == 'POST':
        user_vo = UserVO()
        user_dao = UserDAO()
        user = user_dao.match_user(request.form.get('username'), request.form.get('password'))
        if not user:
            flash("Invalid Credentials")
            return redirect("/login")
        return redirect("/")
