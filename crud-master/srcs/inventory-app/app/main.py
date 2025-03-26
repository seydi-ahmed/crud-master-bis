# crud-master/srcs/inventory-app/app/main.py

from flask import Flask, request, jsonify
from .database import db
from .models import Movie

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:diouf@localhost/movies_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

@app.route('/api/movies', methods=['GET', 'POST', 'DELETE'])
def handle_movies():
    if request.method == 'GET':
        movies = Movie.query.all()
        return jsonify([{"id": m.id, "title": m.title, "description": m.description} for m in movies])
    elif request.method == 'POST':
        data = request.json
        movie = Movie(title=data['title'], description=data['description'])
        db.session.add(movie)
        db.session.commit()
        return jsonify({"id": movie.id}), 201
    elif request.method == 'DELETE':
        Movie.query.delete()
        db.session.commit()
        return '', 204

@app.route('/api/movies/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def handle_movie(id):
    movie = Movie.query.get_or_404(id)
    if request.method == 'GET':
        return jsonify({"id": movie.id, "title": movie.title, "description": movie.description})
    elif request.method == 'PUT':
        data = request.json
        movie.title = data['title']
        movie.description = data['description']
        db.session.commit()
        return jsonify({"id": movie.id})
    elif request.method == 'DELETE':
        db.session.delete(movie)
        db.session.commit()
        return '', 204

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)