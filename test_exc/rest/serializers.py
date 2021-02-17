from rest_framework import serializers

from .models import *



class InterviewSerializer(serializers.ModelSerializer):
    '''Список опросов'''

    class Meta:
        model = Interview
        fields = ("id", "name", "created_at", "end_at")



class QuestionSerializer(serializers.ModelSerializer):
    '''Список вопросов'''

    interview = serializers.SlugRelatedField(slug_field='name', read_only=True)

    class Meta:
        model = Question
        fields = ("id", "text", "type", "interview")



class AnswerListSerializer(serializers.ModelSerializer):
    """Список проголосованных опросов"""

    interview_id = serializers.SlugRelatedField(slug_field='name', read_only=True)

    class Meta:
        model = Answer
        fields = ("id", "interview_id")



class AnswerDetailSerializer(serializers.ModelSerializer):
    """ответы голосования"""

    question_id = serializers.SlugRelatedField(slug_field='text', read_only=True)
    interview_id = serializers.SlugRelatedField(slug_field='id', read_only=True)

    class Meta:
        model = Answer
        fields = '__all__'









