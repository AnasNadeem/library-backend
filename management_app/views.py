from management_app.models import Application
from management_app.serializers import ApplicationSerializer
from rest_framework.generics import APIView
from rest_framework import status, response

class ApplicationSubmit(APIView):
  serializer_class = ApplicationSerializer
  def post(self, request, format=None):
    serializer = self.serializer_class(data=request.data)
    if serializer.is_valid():
      enrol_num = serializer.data.get('enrol_num')
      app_queryset = Application.objects.filter(enrol_num=enrol_num)
      if app_queryset.exists():
        return response.Response({'pending':"Enrollment number already exist."}, status=status.HTTP_200_OK)
      else:
        serializer.save()
        return response.Response({'success':"Form has been submitted"}, status=status.HTTP_201_CREATED)
    return response.Response({'error': "Invalid Data."}, status=status.HTTP_400_BAD_REQUEST)