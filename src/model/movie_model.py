from sqlalchemy import Column, Integer, String, DateTime, Text
from sqlalchemy.orm import declarative_base
import uuid

Base = declarative_base()

class MovieModel(Base):
	def __repr__(self):
		return f'<Movie {self.title}>'

	__tablename__ = "media_movies"

	id = Column('id', Text(length=36), default=lambda: str(uuid.uuid4()), primary_key=True)
	title = Column('title', String)
	overview = Column('overview', Text)
	vote_average = Column('vote_average', Integer)
	img_url = Column('img_url',String)
	release_date = Column('release_date',String)