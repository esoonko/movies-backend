from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import os
from model.movie_model import MovieModel, Base



basedir = os.path.abspath(os.path.dirname(__file__))
engine = create_engine('sqlite:///' + os.path.join(basedir, 'database.db'))
Session = sessionmaker(bind=engine)

def test_movies_get_added_and_retrieved():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
    session = Session()
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

    session.add(movie1)
    session.add(movie2)
    session.commit()

    assert session.query(MovieModel.id).count() == 2

    session.rollback()
    session.close()

def test_get_specific_movie():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
    session = Session()
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

    session.add(movie1)
    session.add(movie2)
    session.commit()
    
    target_id = movie1.id
    target_title = movie1.title

    result = session.query(MovieModel.title).where(MovieModel.id == target_id)

    assert result.first().title == target_title
    assert result.count() == 1

    session.rollback()
    session.close()




