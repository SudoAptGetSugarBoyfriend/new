from rest_framework.views import APIView
from rest_framework.response import Response
from quiz.models import Quiz
from .serializers import QuizApiSerializer

class QuizApiList(APIView):

	def get(self, request):
		quizapis = Quiz.objects.all()
		serializer = QuizApiSerializer(quizapis, many=True)
		return Response(serializer.data)

	def post(self):
		pass