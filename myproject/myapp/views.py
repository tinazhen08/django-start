from django.shortcuts import render
from rest_framework import viewsets
from .models import User, Quiz, Question
from .serializers import UserSerializer, QuizSerializer, QuestionSerializer

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class QuizViewSet(viewsets.ModelViewSet):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer

class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

""" class RoleViewSet(viewsets.ModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer """

""" class TypeViewSet(viewsets.ModelViewSet):     
    queryset = Types.objects.all()
    serializer_class = TypeSerializer """