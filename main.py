from controllers.student_controller import StudentController
from controllers.student_subject_controller import StudentSubjectController
from controllers.subject_controller import SubjectController

student_instance = StudentSubjectController()
response = student_instance.create(student_id=1, subject_id=1)
print(response)