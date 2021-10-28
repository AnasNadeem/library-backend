from library_app.models import (
  Course,
  Book,
  Branch)
from rest_framework.generics import (
  ListAPIView,
  CreateAPIView)
from library_app.serializers import (
  CourseSerializer, 
  BookSerializer,
  BranchSerializer) 
from rest_framework import status
from rest_framework.response import Response

# Create your views here.
class CourseCreateView(CreateAPIView):
  queryset = Course.objects.all()
  serializer_class = CourseSerializer

class CourseListView(ListAPIView):
  queryset = Course.objects.all()
  serializer_class = CourseSerializer

class BookListView(ListAPIView):
  queryset = Book.objects.all()
  serializer_class = BookSerializer

class BookCreateView(CreateAPIView):
  queryset = Book.objects.all()
  serializer_class = BookSerializer

class BranchListView(ListAPIView):
  queryset = Branch.objects.all()
  serializer_class = BranchSerializer

class BranchCreateView(CreateAPIView):
  queryset = Branch.objects.all()
  serializer_class = BranchSerializer
  
# class BookView(APIView):
#   serializer_class = BookSerializer

#   def post(self, request, format=None):
#     serializer = self.serializer_class(data=request.data)
#     if serializer.is_valid():
#       pass
#     return Response({'error':"Invalid data"}, status=status.HTTP_400_BAD_REQUEST)