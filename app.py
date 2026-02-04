import os
from flask import Flask, render_template_string, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

# Configure Database from Environment Variables
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Database Model
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    author = db.Column(db.String(200), nullable=False)

# Create Database Tables
with app.app_context():
    db.create_all()

# Modern Bootstrap UI Template
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Azure Bookcase | Inventory Management</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <style>
        body { background-color: #f4f7f9; font-family: 'Inter', sans-serif; color: #334155; }
        .navbar { background-color: #2c3e50; padding: 1rem 0; box-shadow: 0 2px 4px rgba(0,0,0,0.1); }
        .card { border: none; border-radius: 12px; box-shadow: 0 4px 12px rgba(0,0,0,0.05); }
        .btn-add { background-color: #2D8B9A; color: white; border-radius: 8px; padding: 10px; transition: 0.3s; }
        .btn-add:hover { background-color: #246e7a; color: white; transform: translateY(-1px); }
        .table { background: white; border-radius: 12px; overflow: hidden; }
        .table thead { background-color: #f8fafc; color: #64748b; text-transform: uppercase; font-size: 0.85rem; }
        .delete-link { color: #ef4444; text-decoration: none; font-weight: 500; }
        .delete-link:hover { color: #b91c1c; text-decoration: underline; }
    </style>
</head>
<body>

<nav class="navbar navbar-dark mb-5">
    <div class="container">
        <a class="navbar-brand d-flex align-items-center" href="#">
            <span class="fs-4 fw-bold">📚 Azure Cloud Library</span>
        </a>
    </div>
</nav>

<div class="container pb-5">
    <div class="row g-4">
        <div class="col-lg-4">
            <div class="card p-4">
                <h5 class="fw-bold mb-4">Add New Record</h5>
                <form action="/add" method="POST">
                    <div class="mb-3">
                        <label class="form-label small fw-semibold">Book Title</label>
                        <input type="text" name="title" class="form-control border-light-subtle" placeholder="Enter title" required>
                    </div>
                    <div class="mb-3">
                        <label class="form-label small fw-semibold">Author Name</label>
                        <input type="text" name="author" class="form-control border-light-subtle" placeholder="Enter author" required>
                    </div>
                    <button type="submit" class="btn btn-add w-100 fw-bold mt-2">Add to Database</button>
                </form>
            </div>
        </div>

        <div class="col-lg-8">
            <div class="card p-4">
                <h5 class="fw-bold mb-4">Current Inventory</h5>
                <div class="table-responsive">
                    <table class="table align-middle">
                        <thead>
                            <tr>
                                <th>Book Title</th>
                                <th>Author</th>
                                <th class="text-end">Action</th>
                            </tr>
                        </thead>
                        <tbody>
                            {% for book in books %}
                            <tr>
                                <td class="fw-medium text-dark">{{ book.title }}</td>
                                <td class="text-secondary">{{ book.author }}</td>
                                <td class="text-end">
                                    <a href="/delete/{{ book.id }}" class="delete-link small">Remove</a>
                                </td>
                            </tr>
                            {% else %}
                            <tr>
                                <td colspan="3" class="text-center py-4 text-muted small">No books found in database.</td>
                            </tr>
                            {% endfor %}
                        </tbody>
                    </table>
                </div>
            </div>
        </div>
    </div>
</div>

</body>
</html>
"""

@app.route('/')
def index():
    books = Book.query.all()
    return render_template_string(HTML_TEMPLATE, books=books)

@app.route('/add', methods=['POST'])
def add():
    new_book = Book(title=request.form.get('title'), author=request.form.get('author'))
    db.session.add(new_book)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/delete/<int:id>')
def delete(id):
    book = Book.query.get(id)
    if book:
        db.session.delete(book)
        db.session.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run()
