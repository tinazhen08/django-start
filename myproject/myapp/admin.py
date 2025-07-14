from django.contrib import admin
from .models import Role, User, Types, Quizzes, Questions
# Register your models here.

admin.site.register(Role)
admin.site.register(User)
admin.site.register(Types)
admin.site.register(Quizzes)
admin.site.register(Questions)