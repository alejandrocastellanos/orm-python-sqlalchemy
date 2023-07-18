from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class DBConnection:

    engine = create_engine('postgresql://postgres:@localhost:5432/scrappers', echo=True)

    def session(self):
        session = sessionmaker(bind=self.engine)
        return session()

    def make_migrations(self):
        Base.metadata.create_all(self.engine)
