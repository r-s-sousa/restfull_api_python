from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample data
books = [
    {"id": 1, "title": "Python Programming", "author": "John Doe"},
    {"id": 2, "title": "Flask Framework", "author": "Jane Smith"}
]

# GET method to fetch all books
@app.route('/books', methods=['GET'])
def get_books():
    return jsonify(books)

# GET method to fetch a specific book by ID
@app.route('/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    book = next((book for book in books if book['id'] == book_id), None)
    if book:
        return jsonify(book)
    return jsonify({"error": "Book not found"}), 404

# POST method to add a new book
@app.route('/books', methods=['POST'])
def add_book():
    new_book = request.json
    books.append(new_book)
    return jsonify({"message": "Book added successfully"}), 201

# PUT method to update an existing book
@app.route('/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    book = next((book for book in books if book['id'] == book_id), None)
    if book:
        book.update(request.json)
        return jsonify({"message": "Book updated successfully"})
    return jsonify({"error": "Book not found"}), 404

# DELETE method to delete a book
@app.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    books[:] = [book for book in books if book['id'] != book_id]
    return jsonify({"message": "Book deleted successfully"})

if __name__ == '__main__':
    app.run(debug=True)
