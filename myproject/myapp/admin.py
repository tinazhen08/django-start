from django.contrib import admin
from .models import User, Quizzes, Questions
# Register your models here.

admin.site.register(User)
admin.site.register(Quizzes)
admin.site.register(Questions)