from django.urls import include, path
from django.contrib import admin
from myquiz import views as index_views
from rest_framework.urlpatterns import format_suffix_patterns
from quizapi import views
from rest_framework.permissions import *


urlpatterns = [
	path('', index_views.index),
	path('login/', index_views.login, name='login'),
	path('questions/', index_views.questions, name='questions'),
	path('quizapi/', views.QuizApiList.as_view()),
    path('admin/', admin.site.urls),
]

urlpatterns = format_suffix_patterns(urlpatterns)