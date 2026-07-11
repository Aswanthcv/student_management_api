from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import StudentSerializer
from .models import *

# Create your views here.

class StudentApiView(APIView):
    def get(self, request):
        students = Student.objects.all()
        print(students)
        serializer = StudentSerializer(students, many=True)
        print(serializer.data)
        return Response(serializer.data)

    def post(self, request):

        serializer = StudentSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    