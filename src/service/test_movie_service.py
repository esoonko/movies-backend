from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import os
from model.movie_model import MovieModel, Base
from repository.movie_repository import MovieRepository
from service.movie_service import MovieService

basedir = os.path.abspath(os.path.dirname(__file__))
engine = create_engine('sqlite:///' + os.path.join(basedir, 'database.db'))
Session = sessionmaker(bind=engine)
movie_repository = MovieRepository(Session())
movie_service = MovieService(movie_repository)

def test_movies_get_added_and_retrieved():
	Base.metadata.drop_all(engine)
	Base.metadata.create_all(engine)
	movie1 = MovieModel(title='Bee Movie',
			   overview='BEEMOOVIE',
			   vote_average='4',
			   img_url='test_url1',
			   release_date='2022-10-06')
	
	movie2 = MovieModel(title='Bee Movie 2',
			   overview='Bee Movie should have gotten a sequel',
			   vote_average='5',
			   img_url='test_url2',
			   release_date='2022-10-06')

	movie_service.add_movie(movie1)
	movie_service.add_movie(movie2)

	assert len(movie_service.get_all_movies()) == 2

	movie_service.movie_repository.session.rollback()
	movie_service.movie_repository.session.close()

def test_get_specific_movie():
	Base.metadata.drop_all(engine)
	Base.metadata.create_all(engine)
	movie1 = MovieModel(title='Bee Movie',
			   overview='BEEMOOVIE',
			   vote_average='4',
			   img_url='test_url1',
			   release_date='2022-10-06')
	
	movie2 = MovieModel(title='Bee Movie 2',
			   overview='Bee Movie should have gotten a sequel',
			   vote_average='5',
			   img_url='test_url2',
			   release_date='2022-10-06')

	movie_service.add_movie(movie1)
	movie_service.add_movie(movie2)
	
	target_id = movie1.id
	target_title = movie1.title

	result = movie_repository.find_movie(target_id)
	assert result['title'] == target_title

	movie_service.movie_repository.session.rollback()
	movie_service.movie_repository.session.close()

def test_get_movie_doesnt_exist():
	Base.metadata.drop_all(engine)
	Base.metadata.create_all(engine)
	random_id = '1'

	result = movie_service.find_movie(random_id)
	assert result == None
    
	movie_service.movie_repository.session.rollback()
	movie_service.movie_repository.session.close()
