from django.contrib import admin
from .models import Role, Users, Types, Quizzes, Questions
# Register your models here.

admin.site.register(Role, Users, Types, Quizzes, Questions)