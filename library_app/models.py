from django.db import models

# Create your models here.
class Course(models.Model):
  name = models.CharField(max_length=55)
  tot_sem = models.IntegerField()

class Book(models.Model):
  name = models.CharField(max_length=155)
  course_id = models.ForeignKey(Course, on_delete=models.CASCADE)
  semester = models.IntegerField()
  author_name = models.TextField()

