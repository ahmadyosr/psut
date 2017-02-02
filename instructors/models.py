from django.db import models

class School(models.Model):
	title = models.CharField(max_length=200,blank=True,null=True)
	# Create your models here.

class Role(models.Model):
	title = models.CharField(max_length=200,blank=True,null=True)

class OfficeHours(models.Model):
	office_hour = models.CharField(max_length=200)
	
class Instructor(models.Model):
	school = models.ForeignKey(School,blank=True,null=True)
	role = models.ForeignKey(Role,blank=True,null = True)
	first_name = models.CharField(max_length=200)
	middle_name = models.CharField(max_length=200)
	last_name = models.CharField(max_length=200)
	#data:
	office_hours= models.CharField(max_length=500)
	phone_number= models.CharField(max_length=200, blank= True)
	email= models.CharField(max_length=200)
	notes = models.CharField(max_length=200)
	def __str__(self):
		return "%s%s"% (self.first_name,self.last_name)