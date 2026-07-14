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
        
    def put(self, request,id):
        
        student = Student.objects.get(id=id)
        serializer = StudentSerializer(student,data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
            

        return Response("Invaid object", status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,id):

        student = Student.objects.filter(id=id).first()
        
        if not student:
            return Response("Student not found",status=404)
        student.delete()
        return Response("Student was deleted",status=200)