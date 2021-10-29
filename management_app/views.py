from management_app.models import Application
from management_app.serializers import ApplicationSerializer
from rest_framework.views import APIView
from rest_framework import status, response, generics
from django.contrib.auth.models import User

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
  queryset = Application.objects.all()
  serializer_class = ApplicationSerializer

class UnapprovedApplicationList(APIView):
  '''Pending application list of student to be verified and approved by the teacher.'''
  serializer_class = ApplicationSerializer
  def get(self, request, format=None):
    queryset = Application.objects.filter(is_approved=False)
    serializer = self.serializer_class(data=queryset, many=True)
    serializer.is_valid()
    return response.Response({"data":serializer.data}, status=status.HTTP_200_OK)

class ApprovedApplicationList(APIView):
  '''Pending application list of student to be verified and approved by the teacher.'''
  serializer_class = ApplicationSerializer
  def get(self, request, format=None):
    queryset = Application.objects.filter(is_approved=True)
    serializer = self.serializer_class(data=queryset, many=True)
    serializer.is_valid()
    return response.Response({'data':serializer.data}, status=status.HTTP_200_OK)

class ApproveApplication(APIView):
  '''Approving application of student after verifying their crendentials by the teacher.'''
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
      dob = application.dob
      password = name.split(' ')[0] + dob.split('-')[2]
      User.objects.create(username=enrol_num, password=password)
      return response.Response({"success":"Application approved."}, status=status.HTTP_201_CREATED)
    return response.Response({"error":"Data doesn't exist."}, status=status.HTTP_400_BAD_REQUEST)
    