from flask import render_template, request
from app import app
from models.library import books, add_new_book, remove_book
from models.book import Book

@app.route("/library")
def index():
    return render_template("index.html", title="Home", books=books)

@app.route("/books/<index>")
def single_book(index):
    return render_template("book.html", title="Book", books=books[int(index)])

@app.route("/library", methods=["POST"])
def add_book():
    book_title = request.form['title']
    book_author = request.form['author']
    book_genre =  request.form['genre']
    new_book = Book(book_title, book_author, book_genre)
    add_new_book(new_book)
    return render_template("index.html", title="Home", books=books)

@app.route("/remove/<index>", methods=["POST"])
def remove_book_from_library(index):
    remove_book(int(index))
    return render_template("index.html", title="Home", books=books)