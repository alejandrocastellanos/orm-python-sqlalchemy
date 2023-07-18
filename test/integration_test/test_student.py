import unittest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from orm.clients import Base
from orm.models.student import Student


class StudentTestCase(unittest.TestCase):

    def setUp(self):
        # db in memory
        self.engine = create_engine('sqlite:///:memory:')
        Base.metadata.create_all(bind=self.engine)
        session = sessionmaker(bind=self.engine)
        self.session = session()

    def tearDown(self):
        # drop db after run test
        Base.metadata.drop_all(bind=self.engine)

    def test_create_student(self):
        student = Student(name='Alejandro', age=12)
        self.session.add(student)
        self.session.commit()

        saved_user = self.session.query(Student).first()
        self.assertEqual(saved_user.name, 'Alejandro')
        self.assertEqual(saved_user.age, 12)

    def test_delete_student(self):
        user = Student(name='Jane Smith', age=20)
        self.session.add(user)
        self.session.commit()

        self.session.delete(user)
        self.session.commit()

        deleted_user = self.session.query(Student).first()
        self.assertIsNone(deleted_user)

if __name__ == '__main__':
    unittest.main()
