# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

class School(models.Model):
	title = models.CharField(max_length=200, null = True , blank = True )
	# Create your models here.
	def __unicode__(self):
		return self.title 
		
class Department0(models.Model):
	school = models.ForeignKey(School)
	title = models.CharField(max_length =200 , blank = True , null = True ) 
	def __unicode__(self):
		return self.title 	
		

class OfficeHours(models.Model):
	office_hours = models.CharField(max_length=200)
	def __unicode__(self):
		return self.office_hours

		
class OfficeHours2(models.Model):
	office_hours2 = models.CharField(max_length=200)
	def __unicode__(self):
		return self.office_hours2
	
		
		
class Instructor(models.Model):
	department = models.ForeignKey(Department0,blank=True,null=True)
	school = models.ForeignKey(School,blank=True,null=True)
	arabic_name = models.CharField(max_length=200)
	english_name = models.CharField(max_length=200 , blank=True , null = True )
	email= models.CharField(max_length=200)
	office_hours_1_start = models.ForeignKey(OfficeHours ,blank = True , null = True )#just populate this with officehours beggining time and will  be
	office_hours_2_start = models.ForeignKey(OfficeHours2 ,blank = True , null = True )#just populate this with officehours beggining time and it will  be
	notes = models.CharField(max_length=200,blank = True,null = True)
	visits = models.IntegerField(default = 0 )
	doorsheet =  models.FileField(null= True , blank = True )
	def __unicode__(self):
		return u"%s%s"% (self.arabic_name,self.english_name)
		




		
