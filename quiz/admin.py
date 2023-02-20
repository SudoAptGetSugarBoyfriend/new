from django.contrib import admin
from quiz.models import Quiz

class QuizAdmin(admin.ModelAdmin):
	list_display = ('question',)

admin.site.register(Quiz, QuizAdmin)