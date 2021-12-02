from flask import Flask
from flask import jsonify
from markupsafe import escape
import json
app = Flask(__name__)

book=[
	{
		'id':1,
		'titre' : 'un titre',
	},
	{
		'id':2,
		'titre': 'un autre titre random',
	}
]

books = json.load(open("books.json"))

@app.route("/")
def index():
 
    return 'Hello my app'

@app.route('/about')
def about():

    return 'The about page'

@app.route('/api/book', methods=['GET'])
def all_book():
    return jsonify([book]),200

# @app.route('/api/book/<id>', methods=['GET'])
# def get_book(id):
#     for book in books:
#         if id == book['id']:
#             return jsonify([book.to_json()])
#     return 'this id is not a book'

@app.route('/api/book/<id>', methods=['GET'])
def get_book(id):
    for book_ in books:
        if id == book_['isbn']:
            return jsonify([book_]),200
    return 'this id is not a book'

