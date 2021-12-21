from flask import Flask
from flask_restful import Resource, Api
from services.read_file import read_file
from classes.movie import Movie
from classes.links import Links
from classes.rating import Ratings
from classes.tags import Tags


app = Flask(__name__)
api = Api(app)


class PrintMovies(Resource):
    def get(self):
        data = read_file('./data/movies.csv')
        movies = list()
        for row in data:
            movies.append(Movie(row.split(',')[0], row.split(',')[1], row.split(',')[2]).__dict__)
        return movies


class PrintRatings(Resource):
    def get(self):
        data = read_file('./data/ratings.csv')
        ratings = list()
        for row in data:
            ratings.append(Ratings(row.split(',')[0], row.split(',')[1], row.split(',')[2], row.split(',')[3]).__dict__)
        return ratings


class PrintLinks(Resource):
    def get(self):
        data = read_file('./data/links.csv')
        links = list()
        for row in data:
            links.append(Links(row.split(',')[0], row.split(',')[1], row.split(',')[2]).__dict__)
        return links


class PrintTags(Resource):
    def get(self):
        data = read_file('./data/tags.csv')
        tags = list()
        for row in data:
            tags.append(Tags(row.split(',')[0], row.split(',')[1], row.split(',')[2], row.split(',')[3]).__dict__)
        return tags


api.add_resource(PrintMovies, '/movies')
api.add_resource(PrintRatings, '/ratings')
api.add_resource(PrintLinks, '/links')
api.add_resource(PrintTags, '/tags')

if __name__ == '__main__':
    app.run(debug=True)
