from library_app.models import Course, Book, Branch
from rest_framework.generics import ListAPIView, CreateAPIView
from library_app.serializers import (
  CourseSerializer, 
  BookSerializer,
  BranchSerializer) 
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser, AllowAny

# Create your views here.
class CourseCreateView(CreateAPIView):
  queryset = Course.objects.all()
  serializer_class = CourseSerializer
  permission_classes = [IsAdminUser]

class CourseListView(ListAPIView):
  queryset = Course.objects.all()
  serializer_class = CourseSerializer
  permission_classes = [AllowAny]

class BookListView(ListAPIView):
  queryset = Book.objects.all()
  serializer_class = BookSerializer
  permission_classes = [AllowAny]

class BookCreateView(CreateAPIView):
  queryset = Book.objects.all()
  serializer_class = BookSerializer
  permission_classes = [IsAdminUser]

class BranchListView(ListAPIView):
  queryset = Branch.objects.all()
  serializer_class = BranchSerializer
  permission_classes = [AllowAny]

class BranchCreateView(CreateAPIView):
  queryset = Branch.objects.all()
  serializer_class = BranchSerializer
  permission_classes = [IsAdminUser]
  
# class BookView(APIView):
#   serializer_class = BookSerializer

#   def post(self, request, format=None):
#     serializer = self.serializer_class(data=request.data)
#     if serializer.is_valid():
#       pass
#     return Response({'error':"Invalid data"}, status=status.HTTP_400_BAD_REQUEST)