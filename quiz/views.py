from django.shortcuts import render, redirect
from quiz.models import Quiz

def qpage(request):
	questions = Quiz.objects.all()

	return render(request, 'quiz.html', {'questions': questions})



