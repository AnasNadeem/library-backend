from management_app.models import Application
from management_app.serializers import ApplicationSerializer
from rest_framework.views import APIView
from rest_framework import status, response, generics

class ApplicationSubmit(APIView):
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
  queryset = Application.objects.all()
  serializer_class = ApplicationSerializer

class UnapprovedApplicationList(APIView):
  serializer_class = ApplicationSerializer
  def get(self, request, format=None):
    queryset = Application.objects.filter(is_approved=False)
    serializer = self.serializer_class(data=queryset, many=True)
    return response.Response({'data':serializer.data}, status=status.HTTP_200_OK)

class ApproveApplication(APIView):
  serializer_class = ApplicationSerializer
  def post(self, request, format=None):
    application_id = request.data['id']
    apllication = Application.objects.filter(id=application_id)
    serializer = self.serializer_class(data=apllication)
    if apllication.exists() and serializer.is_valid():
      apllication.is_approved = True
      apllication.save()
      return response.Response({"success":"Application approved."}, status=status.HTTP_201_CREATED)
    return response.Response({"error":"Data doesn't exist."}, status=status.HTTP_400_BAD_REQUEST)
    