from django.urls import path
from student.views import home,candidates_details

urlpatterns = [
    path('', home,name='home'),
    path('candidate/<int:pk>',candidates_details,name='candidates_details')
]