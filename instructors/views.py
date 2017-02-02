# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse , HttpResponseRedirect
from instructors.models import Instructor
import csv, random
from django.core.urlresolvers import reverse
# Create your views here.

def home(request):

	#here to populate with numbers and officehours.
	'''instructors = Instructor.objects.all()
	for instructor in instructors : 
		instructor.phone_number=str(random.randrange(791111111,799999999,987))	
		instructor.office_hours=str(random.randrange(11,30,1))	
		instructor.save()'''
	#uncomment the followuing to populate ?
	file = open('instructors/data.csv','rt')
	reader = csv.reader(file)
	for row in reader  :
		if row[0] and row[1] and row[2]:
			i = Instructor.objects.create(first_name=row[1],last_name=row[2],email=row[0])
			print i.email , i.first_name, i.last_name
	file.close()
	Instructors = Instructor.objects.all()
	return render(request,'instructors/index.html',{'Instructors':Instructors})

def results(request):
	if len(request.GET['search']) > 2 :
		search_term = request.GET['search']
		keywords = search_term.split()
		results_list = Instructor.objects.none()
		#here the search algorithm
		for i in keywords:
			list1= Instructor.objects.filter(first_name__icontains= i)
			list2= Instructor.objects.filter(last_name__icontains= i)
			results_list = results_list | list1 | list2
		
		if results_list.count() > 1 :
			return render(request,'instructors/results.html',{'results_list':results_list})
		elif results_list.count() >0 :
			inst_id = results_list[0].id
			return HttpResponseRedirect(reverse('instructor2',args=[inst_id]))
		else : 
			return HttpResponseRedirect('/home/?search=لا يوجد نتائج بحث ')
	else:
		return HttpResponseRedirect('/home/?search=كلمة البحث قصيرة جدا')
	
	
def instructor(request, id):

	inst =Instructor.objects.get(id= id)
	return render(request,'instructors/instructor.html',{'inst':inst})