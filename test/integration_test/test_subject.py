import unittest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from orm.clients import Base
from orm.models.subject import Subject


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

    def test_create_subject(self):
        subject = Subject(name='Math')
        self.session.add(subject)
        self.session.commit()

        saved_user = self.session.query(Subject).first()
        self.assertEqual(saved_user.name, 'Math')

    def test_update_subject(self):
        subject = Subject(name='Math')
        self.session.add(subject)
        self.session.commit()
        subject.name = 'English'
        self.session.commit()
        self.assertEqual(subject.name, 'English')



    def test_delete_user(self):
        user = Subject(name='Math')
        self.session.add(user)
        self.session.commit()

        self.session.delete(user)
        self.session.commit()

        deleted_user = self.session.query(Subject).first()
        self.assertIsNone(deleted_user)

if __name__ == '__main__':
    unittest.main()