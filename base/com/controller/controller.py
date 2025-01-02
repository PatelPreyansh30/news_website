from flask import render_template, redirect, request, flash
from base import app


@app.route("/", methods=['GET'])
def home():
    return render_template('home.html')


@app.route("/contact-us", methods=['GET'])
def contact_us():
    return render_template('contact.html')


@app.route("/news", methods=['GET'])
def news():
    return render_template("news.html")


@app.route("/add-news", methods=['GET', 'POST'])
def add_news():
    if request.method == 'GET':
        return render_template("add_news.html")
    elif request.method == 'POST':
        return "POST"
