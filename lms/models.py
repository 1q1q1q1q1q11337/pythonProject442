

# Create your models here.
from django.db.models import (Model,
                              CharField,
                              CASCADE,
                              ForeignKey,
                              )


class Curator(Model):
    first_name = CharField(max_length=20)

    def __str__(self):
        return "курат. "+self.first_name
class Direction(Model):
    name = CharField(max_length=20)
    curator = ForeignKey(Curator,
                         on_delete=CASCADE,
                         related_name='direction',
                         )

    def __str__(self):
        return "напр. "+self.name

class Discipline(Model):
    name = CharField(max_length=20)
    direction = ForeignKey(Direction,
                         on_delete=CASCADE,
                         related_name='discipline',
                         )
    def __str__(self):
        return "напр. "+self.name

class Group(Model):
    group_name = CharField(max_length=20)
    copacity = IntegerField(de)
    direction = ForeignKey(Curator,
                         on_delete=CASCADE,
                         related_name='group',
                         )

    def __str__(self):
        return "группа "+self.group_name

class Student (Model):
    surname = CharField(max_length = 10)
    group = ForeignKey(Group,
                       on_delete = CASCADE,
                       related_name = "student")
    def save(self):
        print('potato')
        if self.group.student,count() < self.group.capacity:
            super().save()


