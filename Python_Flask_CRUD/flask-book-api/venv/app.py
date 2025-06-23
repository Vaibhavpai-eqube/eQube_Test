from flask import Flask, request, jsonify, render_template
from models import db, Book
from datetime import datetime
import  re

app = Flask(__name__)   # this is the main Flask application object,  it creates flask application instance.
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:Tatva2025%40@localhost:3306/flask_books'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

# Create DB tables
with app.app_context():
    db.create_all()

@app.route("/")
def index():
    return render_template("index.html")

#@app.route("/home")
#def home():
#   return render_template("home.html")

# form data submission example
@app.route("/form")
def form():
    return render_template("form.html")

# form data display example
@app.route("/formdata", methods=["POST", "GET"])
def formdata():
    if request.method == "POST":
        result = request.form
        name = result.get('name')
        email = result.get('email')
        return render_template("formdata.html", name=name, email=email)
    else:
        return render_template("formdata.html", name=None, email=None)

# eg for dynamic url routing
@app.route('/user/<username>')
def show_user_profile(username):
    if username == 'admin':
        return "Welcome %s" %username
    else:
        return "Welcome %s" %username

def isValid(email):
    regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
    return re.fullmatch(regex, email) is not None

@app.route("/request", methods=["POST"])
def postRequest():
    data = request.get_json()
    email = data.get('email')
    title = data.get('title')

    if not isValid(email):
        return jsonify({'status': 422, 'res': 'failure', 'error': 'Invalid email format'}), 422

    if Book.query.filter_by(title=title).first():
        return jsonify({'status': 404, 'res': f'Book titled "{title}" already exists'}), 404

    new_book = Book(title=title, available=True, timestamp=datetime.utcnow())
    db.session.add(new_book)
    db.session.commit()

    return jsonify({'status': 200, 'res': new_book.serialize(), 'msg': 'Book added successfully'}), 200

@app.route("/request", methods=["GET"])
def getRequest():
    books = Book.query.all()
    return jsonify({
        'status': 200,
        'res': [b.serialize() for b in books],
        'no_of_books': len(books)
    }), 200

@app.route("/request/<int:id>", methods=["GET"])
def getRequestId(id):
    book = Book.query.get(id)
    if not book:
        return jsonify({'status': 404, 'error': f'Book ID {id} not found'}), 404
    return jsonify({'status': 200, 'res': book.serialize()}), 200

@app.route("/request", methods=["PUT"])
def putRequest():
    data = request.get_json()
    book = Book.query.get(data.get('id'))
    if not book:
        return jsonify({'status': 404, 'res': 'Book not found'}), 404

    book.title = data.get('title', book.title)
    book.available = data.get('available', book.available)
    book.timestamp = datetime.utcnow()
    db.session.commit()

    return jsonify({'status': 200, 'res': book.serialize(), 'msg': 'Book updated successfully'}), 200

@app.route("/request/<int:id>", methods=["DELETE"])
def deleteRequest(id):
    book = Book.query.get(id)
    if not book:
        return jsonify({'status': 404, 'res': 'Book not found'}), 404

    db.session.delete(book)
    db.session.commit()

    books = Book.query.all()
    return jsonify({
        'status': 200,
        'res': [b.serialize() for b in books],
        'msg': 'Book deleted successfully',
        'no_of_books': len(books)
    }), 200

if __name__ == '__main__':
    app.run(debug=1)    # Set debug=1 for development, here it automatically reloads the server on code changes
    # app.run(debug=0)  # Set debug=0 for production, you have to run everytime after making changes
