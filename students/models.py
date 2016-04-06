from django.db import models

# Create your models here.

class Section(models.Model):
	name = models.CharField(max_length=50)

	def __str__(self):
		return self.name

class Student(models.Model):
	section = models.ForeignKey(Section)
	first_name = models.CharField(max_length=50, default=None)
	middle_name = models.CharField(max_length=50, default=None)
	last_name = models.CharField(max_length=50, default=None)
	age = models.SmallIntegerField()