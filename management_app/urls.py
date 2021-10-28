from django.urls import path
from management_app.views import ApplicationSubmit,ApplicationList

urlpatterns = [
  path('application/' , ApplicationSubmit.as_view()),
  path('application-list/', ApplicationList.as_view())
]