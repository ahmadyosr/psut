# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse , HttpResponseRedirect
from instructors.models import Instructor , School
import csv, random
from django.core.urlresolvers import reverse
# Create your views here.

def home(request):
	try:
		school = request.GET['school']
	except :
		school = 'it'
	school = School.objects.get(title = school)
	instructors =Instructor.objects.filter(college= school)
	return render(request,'instructors/index.html',{'instructors':instructors})
	
def results(request):
	if len(request.GET['search']) > 2 :
		search_term = request.GET['search']
		keywords = search_term.split()
		results_list = Instructor.objects.none()
		#here the search algorithm
		for i in keywords:
			list1= Instructor.objects.filter(arabic_name__icontains= i)
			list2= Instructor.objects.filter(english_name__icontains= i)
			results_list = results_list | list1 | list2
		
		if results_list.count() > 1 :
			return render(request,'instructors/results.html',{'results_list':results_list})
		elif results_list.count() >0 :
			inst_id = results_list[0].id
			return HttpResponseRedirect(reverse('instructor',args=[inst_id]))
		else : 
			return HttpResponseRedirect('/home/?search=لا يوجد نتائج بحث ')
	else:
		return HttpResponseRedirect('/home/?search=كلمة البحث قصيرة جدا')
	
	
def instructor(request, id):
	inst = Instructor.objects.get(id= id)
	return render(request,'instructors/instructor.html',{'inst':inst})