from orm.models.subject import Subject


class SubjectController:

    def __init__(self):
        self.subject = Subject

    def create(self, name):
        return self.subject().create(name=name)

    def get_all(self):
        return self.subject().get_all()

    def get(self, _id: int):
        return self.subject().get(_id)

    def delete(self, _id: int):
        return self.subject().delete(_id)

    def update(self, subject, name=None):
        subject.name = name
        self.subject().session.commit()

    def filter(self, name):
        instance_filter = self.subject().filter()
        response = instance_filter(
            self.subject.name == name
        ).all()
        return response if len(response) > 0 else []
