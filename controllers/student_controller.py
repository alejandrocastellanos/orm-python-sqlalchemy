from models.student import Student


class StudentController:

    def __init__(self):
        self.student = Student

    def create(self):
        return self.student().create(name='chill', age=29)

    def get_all(self):
        return self.student().get_all()

    def get(self, _id: int):
        return self.student().get(_id)

    def delete(self, _id: int):
        return self.student().delete(_id)

    def update(self, student, name=None, age=None):
        student.name = name
        student.age = age
        self.student().session.commit()

    def filter(self):
        instance_filter = self.student().filter()
        response = instance_filter(
            self.student.name == 'sara'
        ).all()
        return response if len(response) > 0 else []
