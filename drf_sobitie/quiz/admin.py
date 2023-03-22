
from django.contrib import admin

from .models import Quiz, Question, Answer


class AnswerAdmin(admin.TabularInline):
    model = Answer


class QuestionAdmin(admin.TabularInline):
    model = Question
    inlines = [AnswerAdmin]


class QuizAdmin(admin.ModelAdmin):
    inlines = [QuestionAdmin]


admin.site.register(Answer)
admin.site.register(Question)
admin.site.register(Quiz, QuizAdmin)
