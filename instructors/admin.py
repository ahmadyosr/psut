from django.contrib import admin
from instructors.models import School, Instructor , Department0, OfficeHours1, OfficeHours2, OfficeLocations
# Register your models here.
from django.forms import TextInput , ChoiceField
from django.db import models
class InstructorAdmin(admin.ModelAdmin):
	list_display = ('english_name' , 'arabic_name' , 'email' , 'office_hours_1_start' 
	, 'office_hours_2_start', 'department','school','office_location')
	# list_filter = ('department',)
	list_editable = ('english_name' , 'arabic_name' , 'email' 
	, 'office_hours_1_start' , 'office_hours_2_start','department','school','office_location',)
	
	formfield_overrides = {models.CharField: {'widget': TextInput(attrs={'size':'15'})},
	}
	list_display_links = None
	
admin.site.register(School)
admin.site.register(Department0)
admin.site.register(OfficeLocations)
admin.site.register(Instructor,InstructorAdmin)
admin.site.register(OfficeHours1)
admin.site.register(OfficeHours2)