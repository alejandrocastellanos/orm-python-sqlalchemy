from sqlalchemy import Column, Integer, String

from clients import Base, DBConnection


class Student(Base):

    db_connection = DBConnection
    session = db_connection().session()
    __tablename__ = 'student'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)

    def create(self, **kwargs):
        new_student = Student(
            name=kwargs.get('name', None),
            age=kwargs.get('age', None)
        )
        self.session.add(new_student)
        self.session.commit()

    def get_all(self):
        return self.session.query(Student).all()

    def get(self, _id: int):
        return self.session.query(Student).get(_id)

    def delete(self, _id):
        try:
            _get = self.get(_id)
            self.session.delete(_get)
            self.session.commit()
            return True
        except Exception as e:
            return False

    def filter(self):
        return self.session.query(Student).filter

Base.metadata.create_all(Student.db_connection.engine)
