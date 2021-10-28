from django.urls import path
from management_app.views import (
  ApplicationSubmit,
  ApplicationList, 
  ApproveApplication,
  UnapprovedApplicationList)

urlpatterns = [
  path('application/' , ApplicationSubmit.as_view()),
  path('application-list/', UnapprovedApplicationList.as_view()),
  path('all-application-list/', ApplicationList.as_view()),
  path('approve-application/', ApproveApplication.as_view())
]