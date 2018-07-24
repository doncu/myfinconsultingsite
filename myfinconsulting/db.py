from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session
from sqlalchemy.ext.declarative import declarative_base

from myfinconsulting import config

Base = declarative_base()

engine = create_engine(config.DATABASE_URI, pool_recycle=600)

Session = sessionmaker(bind=engine)
session = scoped_session(lambda: Session(autoflush=False, expire_on_commit=False))
