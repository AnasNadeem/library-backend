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

# class Application(models.Model):
#   name = models.CharField(max_length=150)
#   dob = models.CharField(max_length=15)
#   email = models.EmailField(max_length=55)
#   enrol_num = models.CharField(max_length=55, unique=True)
#   course_name = models.CharField(max_length=150)
#   branch_name = models.CharField(max_length=150)
#   session_year = models.CharField(max_length=20)
#   created_at = models.DateTimeField(auto_now_add=True)
#   # fee_receipt = models.
#   # adm_slip = models.

