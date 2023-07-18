from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

from orm.clients import Base, DBConnection
from orm.models.student import Student
from orm.models.subject import Subject


class SubjectStudentRel(Base):

    _db_connection = DBConnection()
    session = _db_connection.session()
    __tablename__ = 'subject_student_rel'

    id = Column(Integer, primary_key=True)
    student_id = Column(Integer, ForeignKey("student.id"))
    subject_id = Column(Integer, ForeignKey("subject.id"))

    def create(self, **kwargs):
        new_student = SubjectStudentRel(
            student_id=kwargs.get('student_id', None),
            subject_id=kwargs.get('subject_id', None)
        )
        self.session.add(new_student)
        self.session.commit()

    def get_all(self):
        return self.session.query(SubjectStudentRel).all()

    def get(self, _id: int):
        return self.session.query(SubjectStudentRel).get(_id)

    def delete(self, _id):
        try:
            _get = self.get(_id)
            self.session.delete(_get)
            self.session.commit()
            return True
        except Exception as e:
            return False

    def filter(self):
        return self.session.query(SubjectStudentRel).filter

# Student.invoices = relationship("SubjectStudentRel", order_by = SubjectStudentRel.id, back_populates = "student")
# Subject.invoices = relationship("SubjectStudentRel", order_by = SubjectStudentRel.id, back_populates = "subject")
# Base.metadata.create_all(DBConnection.engine)
