from django.db import models

from django.urls import reverse
# Create your models here.

class School(models.Model):
    Scname=models.CharField(max_length=100)
    Scprincipal=models.CharField(max_length=100)
    Sclocation=models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.Scname
    
    def get_absolute_url(self):
        return reverse('detail',kwargs={'pk':self.pk})
    
    


class Student(models.Model):
    Sname=models.CharField(max_length=100)
    Sage=models.IntegerField()
    Scname=models.ForeignKey(School,on_delete=models.CASCADE,related_name='panda')

    def __str__(self) -> str:
        return self.Sname















    
    