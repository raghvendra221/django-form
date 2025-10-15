from django.contrib import admin
from student.models import Profile

@admin.register(Profile)
class profilemodeladmin(admin.ModelAdmin):
    list_display =['name','dob','gender','locality','city','pin','state','mobile','email','job_city','profile_image','my_file']


