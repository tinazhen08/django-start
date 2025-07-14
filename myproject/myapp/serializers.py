from rest_framework import serializers
from .models import User, Types, Quizzes, Questions

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'role']

class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Types
        fields = ['id', 'get_id_display']

class QuizSerializer(serializers.ModelSerializer):
    creator = UserSerializer(read_only=True)

    class Meta:
        model = Quizzes
        fields = ['uuid_id', 'title', 'types', 'creator']
        read_only_fields = ['uuid_id']

class QuestionSerializer(serializers.ModelSerializer):
    quiz = serializers.PrimaryKeyRelatedField(queryset=Quizzes.objects.all())

    class Meta:
        model = Questions
        fields = ['uuid_id', 'question', 'answer', 'incorrect', 'quiz']
        read_only_fields = ['uuid_id']

""" class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ['id', 'get_id_display']
        read_only_fields = ['id'] """