"""
URL configuration for lab1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from courses.views import *
from trainees.views import *



# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('courses',coursesList,name='CoursesList'),
#     path('courses/add',courseAdd,name='CoursesAdd'),
#     path('courses/update/<int:ID>',courseUpdate,name='CoursesUpdate'),
#     path('courses/delete/<int:ID>',courseDelete,name='CoursesDelete'),
#     path('trainees',traineesList,name='TraineesList'),
#     path('trainees/add',traineeAdd,name='TraineesAdd'),
#     path('trainees/update/<int:ID>',traineeUpdate,name='TraineesUpdate'), 
#     path('trainees/delete/<int:ID>',traineeDelete,name='TraineesDelete'), 
# ]



urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/',include('myusers.urls')),
    path('courses/', include('courses.urls')),
    path('trainees/', include('trainees.urls')) 
]
