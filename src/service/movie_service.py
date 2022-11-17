class MovieService():

    def __init__(self,movie_repository):
        self.movie_repository = movie_repository

    def add_movie(self, movie):
        if movie:
            self.movie_repository.add_movie(movie)

    def get_all_movies(self):
        return self.movie_repository.get_all_movies()

    def find_movie(self, movie_id):
        return self.movie_repository.find_movie(movie_id)