from flask import Blueprint, render_template, request, redirect, url_for
from . import db
from .models import Book, Author

main = Blueprint('main', __name__)

@main.route('/')
def index():
    books = Book.query.all()
    return render_template('index.html', books=books)

@main.route('/add_book', methods=['GET', 'POST'])
def add_book():
    if request.method == 'POST':
        title = request.form.get('title')
        authors = request.form.get('authors')

        if authors:
            authors = authors.split(',')
        else:
            authors = []

        book = Book(title=title, status='dostępna')
        db.session.add(book)
        db.session.commit()

        for author_name in authors:
            author_name = author_name.strip()
            author = Author.query.filter_by(name=author_name).first()
            if not author:
                author = Author(name=author_name)
                db.session.add(author)
            book.authors.append(author)

        db.session.commit()
        return redirect(url_for('main.index'))

    return render_template('add_book.html')

@main.route('/borrow_book/<int:book_id>', methods=['POST'])
def borrow_book(book_id):
    book = Book.query.get(book_id)
    if book:
        book.status = 'wypożyczona'
        db.session.commit()
    return redirect(url_for('main.index'))

@main.route('/return_book/<int:book_id>', methods=['POST'])
def return_book(book_id):
    book = Book.query.get(book_id)
    if book:
        book.status = 'dostępna'
        db.session.commit()
    return redirect(url_for('main.index'))

@main.route('/clear_books', methods=['POST'])
def clear_books():
    books = Book.query.all()
    for book in books:
        db.session.delete(book)
    db.session.commit()
    return redirect(url_for('main.index'))
