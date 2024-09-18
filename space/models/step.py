from django.db import models
from django.contrib.auth.models import User
from space.models import *
from ckeditor.fields import RichTextField

class StepModel(models.Model):
    stepcreator=models.ForeignKey(User, on_delete=models.CASCADE,related_name="step")
    stepspace=models.ForeignKey(SpaceModel, on_delete=models.CASCADE, related_name="steps", blank=True)
    steptitle=models.CharField(max_length=50, blank=False, null=False)
    stepcontent=RichTextField(max_length=500, blank=False, null=False)
    relatedresource=models.ForeignKey('ResourceModel', on_delete=models.CASCADE, related_name="stepresource", blank=True)    
    created_time=models.DateTimeField(auto_now_add=True, verbose_name="Created Time")
    updated_time=models.DateTimeField(auto_now=True, verbose_name="Updated Time")
 

#This class is for displaying the names of the space in admin panel and database.
    class Meta:
        db_table='step_table' # This name is used for db_table name
        verbose_name_plural="Steps" #This name is used for Admin Panel dashboard
        verbose_name="Steps" #This name is used for Admin Panel messages

#This function is for displaying the title of the spaces in admin panel.
    def __str__(self):
        return str(self.steptitle)