from django.urls import include, path
import quiz.views as quiz_views

urlpatterns = [
	path('', quiz_views.qpage),
]
