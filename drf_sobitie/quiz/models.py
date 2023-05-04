from django.core.validators import FileExtensionValidator
from django.db import models


class Quiz(models.Model):
    name = models.CharField(
        max_length=50, unique=True, blank=False, verbose_name="Название квиза", help_text="введите название квиза"
    )
    description = models.TextField(verbose_name="Описание квиза", help_text="напишите, о чем этот квиз")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Квиз"
        verbose_name_plural = "Квизы"
        db_table = "quiz"


class QuizResult(models.Model):
    quiz_id = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    image = models.ImageField(
        upload_to="quiz_results/%Y/%m/%d/",
        validators=[FileExtensionValidator(allowed_extensions=["jpeg", "jpg", "png", "mp4"])],
        blank=True,
        verbose_name="Изображение",
        help_text="при желании прикрепите картинку",
    )
    text = models.TextField(
        verbose_name="Текст результата.",
        blank=True,
        help_text="этот текст может отличаться в зависимости от кол-ва правильных ответов",
    )
    correct_answer_cnt = models.IntegerField(
        verbose_name="Необходимое кол-во правильных ответов.",
        help_text="при достижении определенного количества определеяет текст результата",
    )

    def __str__(self):
        return f'{self.quiz_id}, результат: {self.text}'

    class Meta:
        verbose_name = "Результат"
        verbose_name_plural = "Результаты"


class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='questions')
    image = models.ImageField(
        upload_to="quiz_quiestions/%Y/%m/%d/",
        validators=[FileExtensionValidator(allowed_extensions=["jpeg", "jpg", "png", "mp4"])],
        blank=True,
        verbose_name="Изображение",
        help_text="при желании прикрепите картинку",
    )
    question_text = models.TextField(
        max_length=250, blank=False, verbose_name="Вопрос", help_text="введите текст вопроса"
    )

    def __str__(self):
        return f'{self.quiz}, вопрос: {self.question_text}'

    class Meta:
        verbose_name = "Вопрос"
        verbose_name_plural = "Вопросы"
        db_table = "question"


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="answers")
    answer_text = models.CharField(max_length=100, blank=False, verbose_name="Ответ", help_text="введите текст ответа")
    is_right = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.question}, ответ: {self.answer_text}'

    class Meta:
        verbose_name = "Ответ"
        verbose_name_plural = "Ответы"
        db_table = "answers"
