from flask import Flask, request, jsonify
import logging
 
app = Flask(__name__)
 
# Set up logging
logging.basicConfig(format='%(asctime)s %(levelname)-8s %(filename)s %(message)s',
    datefmt='%Y-%m-%dT%H:%M:%S',
    level=logging.DEBUG, filename="book.log")
 
# Sample data for books
books = [
    {"id": 1, "title": "Book 1", "author": "Author 1", "genre": "Fiction", "read": False},
    {"id": 2, "title": "Book 2", "author": "Author 2", "genre": "Non-fiction", "read": True},
    {"id": 3, "title": "Book 3", "author": "Author 3", "genre": "Mystery", "read": False},
    {"id": 4, "title": "Book 4", "author": "Author 4", "genre": "Fiction", "read": True},
    {"id": 5, "title": "Book 5", "author": "Author 5", "genre": "Non-fiction", "read": False},
    {"id": 6, "title": "Book 6", "author": "Author 6", "genre": "Mystery", "read": True},
 
]

#Home API
@app.route("/")
def home():
    app.logger.info("Application Started")
    return jsonify(message="Welcome to the Book App!")

#Login API
@app.route("/login")
def login():
    try:
        app.logger.info("User Logged in")
        return jsonify(message="User Logged in")

    except Exception as e:
        app.logger.error(f"Error in Login: {str(e)}")
    return jsonify(error="Internal Server Error"), 500
 
# API to get a list of all books
@app.route('/api/books', methods=['GET'])
def get_books():
    try:
        logging.info("Get all books requested.")
        return jsonify(books)
    except Exception as e:
        logging.error(f"Error in 'get_books' API: {str(e)}")
        return jsonify({"error": "Internal server error"}), 500
 
# API to get details of a specific book
@app.route('/api/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    try:
        logging.info(f"Get details of book with ID {book_id} requested.")
        book = next((b for b in books if b['kl'] == book_id), None)
        if book:
            return jsonify(book)
        else:
            logging.warning(f"Book with ID {book_id} not found.")
            return jsonify({"error": "Book not found"}), 404
    except Exception as e:
        logging.error(f"Error in 'get_book' API: {str(e)}")
        return jsonify({"error": "Internal server error"}), 500
 
# API to add a new book
@app.route('/api/books', methods=['POST'])
def add_book():
    try:
        data = request.get_json()
        if 'title' in data and 'author' in data and 'genre' in data:
            new_book = {
                "id": len(books) + 1,
                "title": data['title'],
                "author": data['author'],
                "genre": data['genre'],
                "read": False
            }
            books.append(new_book)
            logging.info(f"New book added: {new_book}")
            return jsonify(new_book), 201
        else:
            logging.warning("Incomplete data received for adding a new book.")
            return jsonify({"error": "Incomplete data"}), 400
    except Exception as e:
        logging.error(f"Error in 'add_book' API: {str(e)}")
        return jsonify({"error": "Internal server error"}), 500
 
# API to update a book
@app.route('/api/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    try:
        data = request.get_json()
        book = next((b for b in books if b['id'] == book_id), None)
        if book:
            book.update(data)
            logging.info(f"Book with ID {book_id} updated: {book}")
            return jsonify(book)
        else:
            logging.warning(f"Book with ID {book_id} not found for updating.")
            return jsonify({"error": "Book not found"}), 404
    except Exception as e:
        logging.error(f"Error in 'update_book' API: {str(e)}")
        return jsonify({"error": "Internal server error"}), 500
 
# API to delete a book
@app.route('/api/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    try:
        global books
        book = next((b for b in books if b['id'] == book_id), None)
        if book:
            books = [b for b in books if b['id'] != book_id]
            logging.info(f"Book with ID {book_id} deleted.")
            return jsonify({"message": "Book deleted successfully"})
        else:
            logging.warning(f"Book with ID {book_id} not found for deletion.")
            return jsonify({"error": "Book not found"}), 404
    except Exception as e:
        logging.error(f"Error in 'delete_book' API: {str(e)}")
        return jsonify({"error": "Internal server error"}), 500
 
# API to search books by title or author
@app.route('/api/books/search', methods=['GET'])
def search_books():
    try:
        query = request.args.get('query')
        if query:
            result = [b for b in books if query.lower() in b['title'].lower() or query.lower() in b['author'].lower()]
            logging.info(f"Search result for query '{query}': {result}")
            return jsonify(result)
        else:
            logging.warning("Search request received without a query parameter.")
            return jsonify({"error": "Query parameter 'query' is required"}), 400
    except Exception as e:
        logging.error(f"Error in 'search_books' API: {str(e)}")
        return jsonify({"error": "Internal server error"}), 500
 
# API to get books by genre
@app.route('/api/books/genre/<genre>', methods=['GET'])
def get_books_by_genre(genre):
    try:
        result = [b for b in books if b['genre'].lower() == genre.lower()]
        logging.info(f"Get books by genre '{genre}': {result}")
        return jsonify(result)
    except Exception as e:
        logging.error(f"Error in 'get_books_by_genre' API: {str(e)}")
        return jsonify({"error": "Internal server error"}), 500
 
# API to get books sorted by title or author
@app.route('/api/books/sort', methods=['GET'])
def sort_books():
    try:
        sort_by = request.args.get('sort_by', default='title', type=str)
        sorted_books = sorted(books, key=lambda x: x[sort_by])
        logging.info(f"Books sorted by {sort_by}: {sorted_books}")
        return jsonify(sorted_books)
    except Exception as e:
        logging.error(f"Error in 'sort_books' API: {str(e)}")
        return jsonify({"error": "Internal server error"}), 500

# API to Logout
@app.route("/logout")
def logout():
    try:
        app.logger.info("User Logout")
        return jsonify(message="This is API5")
    except Exception as e:
        app.logger.error(f"Error in API5: {str(e)}")
        return jsonify(error="Internal Server Error"), 500
    
if __name__ == "__main__":
    app.run(port=5002,debug=True)