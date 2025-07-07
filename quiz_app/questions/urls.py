from django.urls import path
from . import views

#'question/' - name of url 
#'views.questions - select questions from view
#'name="questions" - doesn't matter

urlpatterns = [
    path('questions/', views.questions, name='questions'),
]