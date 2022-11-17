from model.movie_model import MovieModel

class MovieRepository():

	def __init__(self, session):
		self.session = session

	def add_movie(self, movie):
		self.session.add(movie)
		self.session.commit()

	def get_all_movies(self):
		return [movie.__dict__ for movie in self.session.query(MovieModel).all()]

	def find_movie(self, movie_id):
		result = self.session.query(MovieModel).where(MovieModel.id == movie_id).first()
		if result is None:
			return None
		else:
			return result.__dict__