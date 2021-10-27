from django.urls import path
from management_app.views import ApplicationSubmit

urlpatterns = [
  path('application' , ApplicationSubmit.as_view())
]