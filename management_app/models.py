from django.db import models

# Create your models here.
class Application(models.Model):
  name = models.CharField(max_length=150)
  dob = models.CharField(max_length=15)
  email = models.EmailField(max_length=55)
  enrol_num = models.CharField(max_length=55)
  course_name = models.CharField(max_length=150)
  branch_name = models.CharField(max_length=150)
  session_year = models.CharField(max_length=20)
  created_at = models.DateTimeField(auto_now_add=True)
  # fee_receipt = models.
  # adm_slip = models.

