
from django.contrib import admin

from .models import Answer, Question, Quiz, QuizResult


class AnswerAdmin(admin.ModelAdmin):
    pass


class AnswerInline(admin.TabularInline):
    model = Answer


class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswerInline]


class QuestionInline(admin.TabularInline):
    model = Question


class QuizResultAdmin(admin.ModelAdmin):
    model = QuizResult


class QuizResultInline(admin.TabularInline):
    model = QuizResult


class QuizAdmin(admin.ModelAdmin):
    inlines = [QuestionInline, QuizResultInline]
    search_fields = ("id", "name")


admin.site.register(Answer, AnswerAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Quiz, QuizAdmin)
admin.site.register(QuizResult, QuizResultAdmin)
