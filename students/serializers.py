from rest_framework import serializers
from rest_framework.response import Response

from . models import *

class SectionSerializer(serializers.ModelSerializer):
	# id = serializers.HyperlinkedIdentityField(view_name='api_section_detail', format='html')
	class Meta:
		model = Section
		fields = ('id', 'name', )

class StudentSerializer(serializers.ModelSerializer):
	class Meta:
		model = Student
		fields = ('first_name', 'middle_name', 'last_name', 'section')