from django.urls import path
from .views import * # importing all views

urlpatterns = [
    path('student-api/', StudentAPI.as_view()),
]
