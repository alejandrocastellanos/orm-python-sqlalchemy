from sqlalchemy import Column, Integer, String

from clients import Base, DBConnection


class Subject(Base):

    _db_connection = DBConnection()
    session = _db_connection.session()
    __tablename__ = 'subject'

    id = Column(Integer, primary_key=True)
    name = Column(String)

    def create(self, **kwargs):
        new_student = Subject(
            name=kwargs.get('name', None)
        )
        self.session.add(new_student)
        self.session.commit()

    def get_all(self):
        return self.session.query(Subject).all()

    def get(self, _id: int):
        return self.session.query(Subject).get(_id)

    def delete(self, _id):
        try:
            _get = self.get(_id)
            self.session.delete(_get)
            self.session.commit()
            return True
        except Exception as e:
            return False

    def filter(self):
        return self.session.query(Subject).filter

Base.metadata.create_all(DBConnection.engine)
