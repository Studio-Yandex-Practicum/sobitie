from django.core.validators import FileExtensionValidator
from django.db import models


class Quiz(models.Model):
    title = models.CharField(
        max_length=50,
        unique=True,
        blank=False,
        verbose_name='Название квиза',
        help_text='введите название квиза'
    )
    description = models.TextField(
        verbose_name='Описание квиза',
        help_text='напишите, о чем этот квиз'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    success_text = models.TextField(
        blank=True,
        help_text="Текст при успешном прохождении.",
        verbose_name="этот текст пользователь увидит при успешном прохождении")
    fail_text = models.TextField(
        verbose_name="Текст при неуспешном прохождении.",
        blank=True,
        help_text="этот текст пользователь увидит при неуспешном прохождении")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Квиз'
        verbose_name_plural = 'Квизы'
        db_table = 'quiz'


class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    image = models.ImageField(
        upload_to='quiz_quiestions/%Y/%m/%d/',
        validators=[FileExtensionValidator(allowed_extensions=['jpeg', 'jpg', 'png', 'mp4'])],
        blank=True,
        verbose_name='Изображение',
        help_text='при желании прикрепите картинку'
    )
    question_text = models.TextField(
        max_length=250,
        blank=False,
        verbose_name='Вопрос',
        help_text='введите текст вопроса')

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'
        db_table = 'question'


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')
    answer_text = models.CharField(
        max_length=100,
        blank=False,
        verbose_name='Ответ',
        help_text='введите текст ответа'
    )
    is_right = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'
        db_table = 'answers'
