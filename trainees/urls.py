from django.contrib import admin
from django.urls import path
from trainees.views import *



urlpatterns = [
    path('',traineesList,name='TraineesList'),
    path('add',traineeAdd,name='TraineesAdd'),
    path('update/<int:ID>',traineeUpdate,name='TraineesUpdate'), 
    path('delete/<int:ID>',traineeDelete,name='TraineesDelete'), 
    # path('',TraineeGErtnic.as_view(), name='TraineesList'),
    # path('update/<int:ID>',TraineeGErtnic.as_view(), name='TraineesUpdate'), 
    # path('add',TraineeGErtnic.as_view(), name='TraineesAdd'),
    # path('delete/<int:ID>',TraineeGErtnic.as_view(), name='TraineesDelete'), 
]

