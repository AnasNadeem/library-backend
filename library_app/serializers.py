from rest_framework.serializers import ModelSerializer 
from library_app.models import Course, Book

class CourseSerializer(ModelSerializer):
  class Meta:
    model = Course
    fields = ['id', 'name', 'tot_sem']

