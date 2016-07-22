from django.shortcuts import render
from django.http import HttpResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from . serializers import *

# Create your views here.
def home(request):
	template = 'students/index.html'
	context_dict = {}
	return render(request, template, context_dict)
	# return HttpResponse("HOME PAGE")

# class api_section(APIView):
# 	serializer_class = SectionSerializer

# 	# def post(self, request, *args, **kwargs):
#  #        serializer = self.serializer_class(data=request.data)
#  #        serializer.is_valid(raise_exception=True)
#  #        user = serializer.validated_data['user']
#  #        token, created = Token.objects.get_or_create(user=user)
#  #        return Response({'token': token.key})
# api_section = api_section.as_view()

@api_view(['GET', 'POST'])
def api_section(request):
	"""
		GET request gets all the sections with its details...
		POST request adds a new section, Example: {"name": "it-b"}...
	"""
	if request.method == 'GET':
		sections = Section.objects.all()
		serializer = SectionSerializer(sections, many=True)
		return Response(serializer.data)

	elif request.method == 'POST':
		serializer = SectionSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			serializer_data = serializer.data
			# del serializer_data['id']
			return Response(serializer_data, status=status.HTTP_201_CREATED)
		else:
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'DELETE', 'PUT'])
def api_section_detail(request, pk):
	"""
PLEASE be aware that <pk> is the id of that certain section...

GET request gets a section and its details through an id...

PUT request updates a section using id as an identifier, Example: {"name": "it-a"}...

DELETE request deletes a section using id as an identifier...

TAKE NOTE: that the pk is supposed to be an integer...

	"""
	try:
		section = Section.objects.get(pk=pk)
		serializer = SectionSerializer(section)
		serializer_data = serializer.data
		# del serializer_data['id']
	except Section.DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND)

	if request.method == 'GET':
		return Response(serializer.data)
	elif request.method == 'DELETE':
		section.delete()
		return Response(serializer_data, status=status.HTTP_200_OK)
	elif request.method == 'PUT':
		serializer = SectionSerializer(section, data=request.data)
		if serializer.is_valid():
			serializer.save()
			serializer_data = serializer.data
			# del serializer_data['id']
			return Response(serializer_data, status=status.HTTP_200_OK)
		else:
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def api_students(request):
	"""
		GET request gets all the students with its details...
		POST request adds a new student, Example: {"section":1, "first_name":"dean", "last_name":"armada", "middle_name":"guinto", "age":24}...
		TAKE NOTE: that the section value must come from a select option value from the front-end...
	"""
	if request.method == 'GET':
		students = Student.objects.all()
		serializer = StudentSerializer(students, many=True)
		return Response(serializer.data)

	elif request.method == 'POST':
		serializer = StudentSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			serializer_data = serializer.data
			# del serializer_data['id']
			return Response(serializer_data, status=status.HTTP_201_CREATED)
		else:
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def api_students_detail(request, pk):
	"""
		PLEASE be aware that <pk> is the id of that certain student...
		GET request gets a student and its details through an id...
		PUT request updates a student using id as an identifier, Example: {"section":2, "first_name":"deans", "last_name":"armadas", "middle_name":"guintos", "age":23}...
		DELETE request deletes a student using id as an identifier...
		TAKE NOTE: that the pk is supposed to be an integer...
		TAKE NOTE: that the section value must come from a select option value from the front-end...
	"""
	try:
		student = Student.objects.get(pk=pk)
		serializer = StudentSerializer(student)
		serializer_data = serializer.data
		# del serializer_data['id']
	except Student.DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND)

	if request.method == 'GET':
		return Response(serializer.data)
	elif request.method == 'DELETE':
		student.delete()
		return Response(serializer_data, status=status.HTTP_200_OK)
	elif request.method == 'PUT':
		serializer = StudentSerializer(student, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer_data, status=status.HTTP_200_OK)
		else:
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)