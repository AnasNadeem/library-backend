from management_app.models import Application, BookSession
from management_app.serializers import ApplicationSerializer, BookSerializer
from rest_framework.views import APIView
from rest_framework import status, response, generics
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from datetime import date
class ApplicationSubmit(APIView):
  '''Submitting the application of the student for their Library card with their details.'''
  serializer_class = ApplicationSerializer
  def post(self, request, format=None):
    serializer = self.serializer_class(data=request.data)
    if serializer.is_valid():
      enrol_num = serializer.data.get('enrol_num')
      #Check if the application with the enrollment number already exist.
      application = Application.objects.filter(enrol_num=enrol_num)
      if application.exists():
        return response.Response({'pending':"Your form is in pending. Contact the teacher."}, status=status.HTTP_200_OK)
      else:
        name = serializer.data.get('name')
        dob = serializer.data.get('dob')
        email = serializer.data.get('email')
        enrol_num = serializer.data.get('enrol_num')
        course_name = serializer.data.get('course_name')
        branch_name = serializer.data.get('branch_name')
        session_year = serializer.data.get('session_year')
        #Create new application 
        new_application = Application()
        new_application.name = name
        new_application.dob = dob
        new_application.email = email
        new_application.enrol_num = enrol_num
        new_application.course_name = course_name
        new_application.branch_name = branch_name
        new_application.session_year = session_year
        new_application.save()
        return response.Response({'success':"Form has been submitted"}, status=status.HTTP_201_CREATED)
    return response.Response({'error': "Invalid Data."}, status=status.HTTP_400_BAD_REQUEST)

class ApplicationList(generics.ListAPIView):
  '''All the application list.'''
  permission_classes = [IsAdminUser]
  queryset = Application.objects.all()
  serializer_class = ApplicationSerializer

class UnapprovedApplicationList(APIView):
  '''Pending application list of student to be verified and approved by the teacher.'''
  serializer_class = ApplicationSerializer
  permission_classes = [IsAdminUser]
  def get(self, request, format=None):
    queryset = Application.objects.filter(is_approved=False)
    serializer = self.serializer_class(data=queryset, many=True)
    serializer.is_valid()
    return response.Response(serializer.data, status=status.HTTP_200_OK)

class ApprovedApplicationList(APIView):
  '''Approved application list of student to be verified and approved by the teacher.'''
  permission_classes = [IsAdminUser]
  serializer_class = ApplicationSerializer
  def get(self, request, format=None):
    queryset = Application.objects.filter(is_approved=True)
    serializer = self.serializer_class(data=queryset, many=True)
    serializer.is_valid()
    return response.Response(serializer.data, status=status.HTTP_200_OK)

class ApproveApplication(APIView):
  '''Approving application of student after verifying their crendentials by the teacher.'''
  permission_classes = [IsAdminUser]
  def post(self, request, format=None):
    application_id = request.data['id']
    application = Application.objects.filter(id=application_id)
    if application.exists():
      application = application[0]
      application.is_approved = True
      application.save()
      # Creating user of student application with enrollment number as username and password as First name and dob year.
      enrol_num = application.enrol_num
      name = application.name
      email = application.email
      dob = application.dob
      password = name.split(' ')[0] + dob.split('-')[2]
      User.objects.create(username=enrol_num, email=email, password=password)
      return response.Response({"success":"Application approved."}, status=status.HTTP_201_CREATED)
    return response.Response({"error":"Data doesn't exist."}, status=status.HTTP_400_BAD_REQUEST)
    
class DismissApplication(APIView):
  '''Dismissing application of student after verifying their crendentials by the teacher.'''
  permission_classes = [IsAdminUser]
  def post(self,request, format=None):
    application_id = request.data['id']
    application = Application.objects.filter(id=application_id)
    if application.exists():
      application = application[0]
      application.delete()
      return response.Response({'success':"Application dismissed."}, status=status.HTTP_200_OK)
    return response.Response({"error":"Data doesn't exist."}, status=status.HTTP_400_BAD_REQUEST)
    
class BookApplicationList(generics.ListAPIView):
  '''All the books with the users list.'''
  permission_classes = [IsAdminUser]
  queryset = BookSession.objects.all()
  serializer_class = BookSerializer

class UserAskForBook(APIView):
  '''User apply for book.'''
  permission_classes = [IsAuthenticated]
  def post(self, request, format=None):
    book_id = request.data['id']
    # Can get the application detail through the enrol num as it is the username of user
    username = request.user.username
    application = Application.objects.filter(enrol_num=username)
    if application.exists():
      application_id = application[0].id
      # Creating a book session 
      book_session = BookSession()
      book_session.book = book_id
      book_session.student = application_id
      book_session.book_status = 'pending'
      book_session.save()
      return response.Response({"success":"Book has been ordered.Visit the library and get it issued."}, status=status.HTTP_201_CREATED)
    return response.Response({"error":"Student doesn't exist."}, status=status.HTTP_400_BAD_REQUEST)
    
class UserBookList(APIView):
  '''All the book of a user list.'''
  permission_classes = [IsAuthenticated]
  serializer_class = BookSerializer
  def get(self, request, format=None):
    username = request.user.username
    application = Application.objects.filter(enrol_num=username)
    application_id = application[0].id
    book_session_list = BookSession.objects.filter(student=application_id)
    serializer = self.serializer_class(data=book_session_list, many=True)
    serializer.is_valid()
    # 1. Check if the book is issued 
    issued_book_list = book_session_list.filter(book_status='issued')
    # 2. If, then check the issued date and if the crnt date longs to 30days then change the book_status to due
    if issued_book_list.exists():
      for book in issued_book_list:
        if (date.today() - book.issued_at) >30:
          book.book_status = 'due'
          book.save()
    # Else show the data.
    return response.Response(serializer.data, status=status.HTTP_200_OK)

class IssuePendingBook(APIView):
  ''' Admin issue the pending book.'''
  permission_classes = [IsAdminUser]
  serializer_class = BookSerializer
  def post(self, request, format=None):
    serializer = self.serializer_class(data=request.data)
    if serializer.is_valid():
      book_id = request.data['book']
      student_app_id = request.data['student']
      book_session = BookSession.ojbects.filter(book=book_id,student=student_app_id)
      if book_session.exists():
        book_session = book_session[0]
        book_session.book_status = 'issued'
        book_session.save()
        return response.Response({"success":"Book has been issued."}, status=status.HTTP_201_CREATED)
      return response.Response({"error":"No data exists."}, status=status.HTTP_400_BAD_REQUEST)
    return response.Response({"error":"Data not valid."}, status=status.HTTP_400_BAD_REQUEST)

class ReturnBook(APIView):
  ''' Admin accept the book and update book_session to returned.'''
  permission_classes = [IsAdminUser]
  serializer_class = BookSerializer
  def post(self, request, format=None):
    serializer = self.serializer_class(data=request.data)
    if serializer.is_valid():
      book_id = request.data['book']
      student_app_id = request.data['student']
      book_session = BookSession.ojbects.filter(book=book_id,student=student_app_id)
      if book_session.exists():
        book_session = book_session[0]
        book_session.book_status = 'returned'
        book_session.save()
        return response.Response({"success":"Book has been returned."}, status=status.HTTP_201_CREATED)
      return response.Response({"error":"No data exists."}, status=status.HTTP_400_BAD_REQUEST)
    return response.Response({"error":"Data not valid."}, status=status.HTTP_400_BAD_REQUEST)

class IssueNewBook(APIView):
  permission_classes = [IsAdminUser]
  def post(self, request, format=None):
    student_id = request.data.get('student_id')
    book_id = request.data.get('book_id')
    book_status = 'issued'
    # Check if book has already been issued or pending 
    book_application = BookSession.objects.filter(student=student_id, book=book_id)
    if book_application.exists():
      crnt_status = book_application.book_status
      return response.Response({"data":f"Book is already in {crnt_status} mode."}, status=status.HTTP_200_OK)

    try:
      book = BookSession()
      book.book = book_id
      book.student = student_id
      book.book_status = book_status
      book.issued_at = date.today()
      book.save()

      return response.Response({'success':"Book has been issued."}, status=status.HTTP_201_CREATED)
    except Exception as e:
      return response.Response({'error':f"{e}"}, status=status.HTTP_400_BAD_REQUEST)

