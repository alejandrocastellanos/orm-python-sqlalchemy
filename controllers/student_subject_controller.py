from models.student_subject_rel import SubjectStudentRel


class StudentSubjectController:

    def __init__(self):
        self.subject_student_rel = SubjectStudentRel

    def create(self, student_id, subject_id):
        return self.subject_student_rel().create(student_id=student_id, subject_id=subject_id)
