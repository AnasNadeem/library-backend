from django.db import models
from library_app.models import Book
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
  is_approved = models.BooleanField(default=False)
  # fee_receipt = models.
  # adm_slip = models.

BOOK_STATUS = (
    ('pending', 'pending'),
    ('issued', 'issued'),
    ('due', 'due'),
    ('returned', 'returned')
)

class BookSession(models.Model):
  book = models.ForeignKey(Book, on_delete=models.CASCADE)
  student = models.ForeignKey(Application, on_delete=models.CASCADE)
  book_status = models.CharField(max_length=55, choices=BOOK_STATUS)
  issued_at = models.DateField(null=True, blank=True)
  returned_at = models.DateField(null=True, blank=True)

  
