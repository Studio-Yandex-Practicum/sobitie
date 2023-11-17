from django import forms
from django.contrib import admin
from django.core.exceptions import ValidationError
from django.urls import reverse
from django.utils.html import format_html
from django.utils.http import urlencode

from .models import Answer, Question, Quiz, QuizResult


class RequiredFormSet(forms.models.BaseInlineFormSet):
    def init(self, *args, **kwargs):
        super(RequiredFormSet, self).init(*args, **kwargs)
        self.forms[0].empty_permitted = False

    def clean(self) -> None:
        super(RequiredFormSet, self).clean()
        is_right = 0
        for form in self.forms:
            if form.cleaned_data.get("is_right"):
                is_right += 1
        if is_right > 1:
            raise ValidationError("Нельзя установить более одного верного ответа")
        if is_right == 0:
            raise ValidationError("Укажите правильный ответ")


class AnswerInline(admin.TabularInline):
    model = Answer
    formset = RequiredFormSet
    fields = (
        "answer_text",
        "is_right",
    )


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswerInline]
    fields = (
        "quiz",
        "image",
        "question_text",
    )
    list_filter = ("quiz_id",)


@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    list_display = ("name", "show_questions")
    list_filter = ("name",)

    def show_questions(self, obj):
        count = Question.objects.filter(quiz_id=obj).count()
        url = (
            reverse("admin:quiz_question_changelist")
            + "?"
            + urlencode({"quiz_id__id": f"{obj.id}"})
        )
        return format_html('<a href="{}">{} Выпроса</a>', url, count)

    show_questions.short_description = "Кол-во вопросов"


@admin.register(QuizResult)
class QuizResultAdmin(admin.ModelAdmin):
    list_filter = ("quiz_id",)
