from django.urls import path
from management_app.views import (
  ApplicationSubmit,
  ApplicationList, 
  ApproveApplication,
  UnapprovedApplicationList,
  ApprovedApplicationList)

urlpatterns = [
  path('application/' , ApplicationSubmit.as_view()),
  path('pending-application-list/', UnapprovedApplicationList.as_view()),
  path('approved-application-list/', ApprovedApplicationList.as_view()),
  path('all-application-list/', ApplicationList.as_view()),
  path('approve-application/', ApproveApplication.as_view())
]