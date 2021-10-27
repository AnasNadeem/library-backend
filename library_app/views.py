from library_app.models import (
  Course,
  Book)
from rest_framework.generics import (
  ListAPIView,
  CreateAPIView)
from library_app.serializers import CourseSerializer

# Create your views here.
class CourseCreateView(CreateAPIView):
  queryset = Course.objects.all()
  serializer_class = CourseSerializer

class CourseListView(ListAPIView):
  queryset = Course.objects.all()
  serializer_class = CourseSerializer