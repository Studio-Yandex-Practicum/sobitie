
from django.contrib import admin

from .models import Answer, Question, Quiz, QuizResult


class AnswerAdmin(admin.ModelAdmin):
    pass
    list_filter = ("question",)


class AnswerInline(admin.TabularInline):
    model = Answer


class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswerInline]
    list_filter = ("quiz_id",)


class QuestionInline(admin.TabularInline):
    model = Question


class QuizResultAdmin(admin.ModelAdmin):
    model = QuizResult
    list_filter = ("quiz_id",)


class QuizResultInline(admin.TabularInline):
    model = QuizResult


class QuizAdmin(admin.ModelAdmin):
    inlines = [QuestionInline, QuizResultInline]
    list_filter = ("name",)


admin.site.register(Answer, AnswerAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Quiz, QuizAdmin)
admin.site.register(QuizResult, QuizResultAdmin)
