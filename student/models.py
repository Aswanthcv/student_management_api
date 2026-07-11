from django.db import models

# Create your models here.

COURSE_CHOICES = [
  ('Python','Python'),
  ('Mern','Mern'),
  ('Spring boot','Spring boot'),

]

class Student(models.Model):
  name = models.CharField(max_length=20)
  age = models.IntegerField()
  place = models.CharField(max_length=30)
  course = models.CharField(
    max_length=15,
    choices=COURSE_CHOICES,
    default = 'Python')

  def __str__(self):
    return self.name