from rest_framework.serializers import ModelSerializer 
from library_app.models import Course, Book, Branch

class CourseSerializer(ModelSerializer):
  class Meta:
    model = Course
    fields = "__all__"

class BranchSerializer(ModelSerializer):
  class Meta:
    model = Branch
    fields = "__all__"

  def to_representation(self, instance):
    response = super().to_representation(instance)
    response['course'] = CourseSerializer(instance.course_id).data
    return response

class BookSerializer(ModelSerializer):
  class Meta:
    model = Book
    fields = "__all__"

  def to_representation(self, instance):
    response = super().to_representation(instance)
    response['branch'] = BranchSerializer(instance.branch_id).data
    return response