from django.db import models
from django.contrib.auth.models import User


CHOICES_TYPE_QUESTION = [
    ("Ответ текстом", "Ответ текстом"),
    ("Ответ с одним вариантом", "Ответ с одним вариантом"),
    ("Ответ с несколькими вариантами", "Ответ с несколькими вариантами"),
]



class Interview(models.Model):
    """Модель опроса"""

    name = models.CharField("Название опроса", max_length = 256)
    created_at = models.DateTimeField(auto_now_add=True)
    end_at = models.DateTimeField()

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = "Опрос"
        verbose_name_plural = "Опросы"



class Question(models.Model):
    """Модель вопроса"""

    text = models.TextField("Текст вопроса")
    type = models.CharField("Тип вопроса", max_length=64, choices = CHOICES_TYPE_QUESTION)
    interview = models.ForeignKey(Interview, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.text[:30])

    class Meta:
        verbose_name = "Вопрос"
        verbose_name_plural = "Вопросы"



class Answer(models.Model):
    """Модель ответа пользователя"""

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    interview_id = models.ForeignKey(Interview, on_delete=models.CASCADE)
    question_id = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer_text = models.TextField("Ответ")

    def __str__(self):
        return "{}: {}".format(self.interview_id.name, self.answer_text)

    class Meta:
        verbose_name = "Ответ пользователя"
        verbose_name_plural = "Ответы пользователей"






    




