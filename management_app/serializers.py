from rest_framework.serializers import ModelSerializer
from management_app.models import Application, BookSession

class ApplicationSerializer(ModelSerializer):
  class Meta:
    model = Application
    fields = "__all__"

class BookSerializer(ModelSerializer):
  class Meta:
    model = BookSession
    fields = "__all__"
