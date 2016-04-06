from django.shortcuts import render
from django.http import HttpResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from . serializers import *

# Create your views here.
def home(request):
	template = 'students/index.html'
	context_dict = {}
	return render(request, template, context_dict)
	# return HttpResponse("HOME PAGE")

@api_view(['GET', 'POST'])
def api_section(request):
	if request.method == 'GET':
		sections = Section.objects.all()
		serializer = SectionSerializer(sections, many=True)
		return Response(serializer.data)

	elif request.method == 'POST':
		serializer = SectionSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			serializer_data = serializer.data
			del serializer_data['id']
			return Response(serializer_data, status=status.HTTP_201_CREATED)
		else:
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	# elif request.method == 'DELETE':
	# 	print ("DEAN")
	# return HttpResponse("API View for sections")

@api_view(['GET', 'DELETE', 'PUT'])
def api_section_detail(request, pk):
	# print (pk)
	try:
		section = Section.objects.get(pk=pk)
		serializer = SectionSerializer(section)
		serializer_data = serializer.data
		del serializer_data['id']
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
			serializer_data = serializer.data
			del serializer_data['id']
			return Response(serializer_data, status=status.HTTP_200_OK)
		else:
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def api_students(request):
	# if request.method == 'GET':

	return HttpResponse("API View for students")