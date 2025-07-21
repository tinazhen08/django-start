from rest_framework import serializers
from .models import User, Quiz, Question

MULTIPLE_CHOICE = 1
TRUE_OR_FALSE = 2 
DROPDOWN = 3 #fill in the blank but without typing
NUMERICAL = 4

TYPE_CHOICES = ((MULTIPLE_CHOICE, 'multiple choice'), (TRUE_OR_FALSE, ' true or false'), (DROPDOWN, 'dropdown'), (NUMERICAL, 'numerical'))

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'role', 'password']

class QuizSerializer(serializers.ModelSerializer):
    #creator = UserSerializer(read_only=True)

    class Meta:
        model = Quiz
        fields = ['title', 'types', 'creator']

    def validate_types(self, value):
        valid_choices = [1, 2, 3, 4]
        if not isinstance(value, list): #check if value is a list
            raise serializers.ValidationError("Expected 'status' to be a list.")
        if not set(value).issubset(valid_choices): #check to see if the values in value is included in valid_choices
            raise serializers.ValidationError("Invalid choice in 'status'.")
        results = []
        for n in value:
            results.append(TYPE_CHOICES[n-1][1]) #get the string representation of the choice
        return results

class QuestionSerializer(serializers.ModelSerializer):
    quiz = serializers.PrimaryKeyRelatedField(queryset=Quiz.objects.all())

    class Meta:
        model = Question
        fields = ['question', 'answer', 'incorrect', 'quiz']

""" class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ['id', 'get_id_display']
        read_only_fields = ['id'] """

""" class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Types
        fields = ['id', 'get_id_display'] """