from django.shortcuts import render
from rest_framework import viewsets
from .models import User, Types, Quizzes, Questions
from .serializers import UserSerializer, TypeSerializer, QuizSerializer, QuestionSerializer

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class TypeViewSet(viewsets.ModelViewSet):     
    queryset = Types.objects.all()
    serializer_class = TypeSerializer

class QuizViewSet(viewsets.ModelViewSet):
    queryset = Quizzes.objects.all()
    serializer_class = QuizSerializer

class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Questions.objects.all()
    serializer_class = QuestionSerializer

""" class RoleViewSet(viewsets.ModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer """