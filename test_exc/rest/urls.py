from django.urls import path

from . import views



urlpatterns = [
    # Food urls
    path("interviews/", views.InterviewListView.as_view(), name="api-interviewlist"),
    path("interviews/<int:pk>", views.InterviewDetailView.as_view(), name="api-interviewdetail"),
    path("interviews/answer/", views.AnswerDetailView.as_view(), name="api-answerviewdetail"),
]

