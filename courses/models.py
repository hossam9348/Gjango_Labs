from django.db import models

# Create your models here.
class Course(models.Model):
    id=models.AutoField(primary_key=True,db_column='ID')
    name=models.CharField(max_length=100,default='palpala',db_column='Name')