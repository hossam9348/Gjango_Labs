from django.contrib import admin
from django.urls import path
from courses.views import *


urlpatterns = [
    path('',coursesList,name='CoursesList'),
    path('add',courseAdd,name='CoursesAdd'),
    path('update/<int:ID>',courseUpdate,name='CoursesUpdate'),
    path('delete/<int:ID>',courseDelete,name='CoursesDelete'),
]
