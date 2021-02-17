from rest_framework.response import Response
from rest_framework.views import APIView
from django.views.generic import View

from .models import *
from .serializers import *



class InterviewListView(APIView):
    '''Вывод опросов'''

    def get(self, request):
        interview = Interview.objects.all()
        serializer = InterviewSerializer(interview, many=True)
        return Response(serializer.data)



class InterviewDetailView(APIView):
    '''вывод опроса'''

    def get(self, request, pk):
        questions = Question.objects.filter(interview_id=pk)
        serializer = QuestionSerializer(questions, many=True)
        return Response(serializer.data)



class AnswerListView(APIView):
    '''Вывод опросов в которых участвовал пользователь'''

    def get(self, request):
        interviews = Question.objects.filter(user=request.user)
        serializer = AnswerListSerializer(interviews, many=True)
        return Response(serializer.data)



class AnswerDetailView(APIView):
    """Вывод информации голосования в опросе"""

    def get(self, request):
        answers = Question.objects.filter(user=request.user)
        serializer = AnswerListSerializer(interviews, many=True)
        return Response(serializer.data)

    def post(self, request):

        try:
            #user = request.user
            interview = dict(request.POST)
            
            for key, value in interview.items():
                if(key != "csrfmiddlewaretoken"):
                    print("asdasd", key)
                    question = Question.objects.get(id=int(key))
                    print("GGG", question.interview.id)
                    print("user: ", request.user)
                    print("value: ", value)
                    Answer.objects.create(
                        user = request.user,
                        interview_id = question.interview.id,
                        question_id = int(key),
                        answer_text = value[0]
                    )

            return Response("Успешно!")

        except:
            return Response("Ошибка сохранения!")









