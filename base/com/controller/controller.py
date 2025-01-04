from flask import render_template, redirect, request, flash, session
from base import app
from base.com.vo import UserVO, NewsVO
from base.com.dao import UserDAO, NewsDAO

@app.route("/", methods=['GET'])
def home():
    return render_template('home.html', show_navigation=True, user=session.get('user'))


@app.route("/contact-us", methods=['GET'])
def contact_us():
    return render_template('contact.html', show_navigation=True, user=session.get('user'))


@app.route("/news", methods=['GET'])
def news():
    news_dao = NewsDAO()
    news = news_dao.view()
    return render_template("news.html", show_navigation=True, user=session.get('user'), news=news)


@app.route("/edit", methods=['GET'])
def news_edit():
    id = request.args.get("news")
    news_dao = NewsDAO()
    news = news_dao.get(id)
    return render_template("add_news.html", show_navigation=True, user=session.get('user'), news=news)


@app.route("/add-news", methods=['GET', 'POST'])
def add_news():
    if request.method == 'GET' and session.get('user') is not None:
        return render_template("add_news.html", show_navigation=True, user=session.get('user'))
    elif request.method == 'POST':
        news_vo = NewsVO()
        news_dao = NewsDAO()
        news_vo.headline = request.form.get('headline')
        news_vo.author_name = request.form.get('author')
        news_vo.description = request.form.get('description')
        news_vo.category = request.form.get('category')
        news_dao.insert(news_vo)
        flash("News added successfully.")
        return redirect("/news")

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
        session['user'] = user.as_dict()
        return redirect("/")
    
    
@app.route("/logout", methods=['GET'])
def logout():
    flash("Logout successfully")
    session.clear()
    return redirect("/")
