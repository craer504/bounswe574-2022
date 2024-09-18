from django.db import models
from django.contrib.auth.models import User
from space.models import SpaceModel
from ckeditor.fields import RichTextField

class ResourceModel(models.Model):
    resourcecreator=models.ForeignKey(User, on_delete=models.CASCADE,related_name="resource")
    resourcespace=models.ForeignKey(SpaceModel, on_delete=models.CASCADE, related_name="resources", blank=True)
    resourcename=models.CharField(max_length=50, blank=False, null=False)
    resourceinfo=RichTextField(max_length=5000, blank=True, null=True)
    resourceattachment=models.FileField(upload_to="files_resource",blank=True, null=True)
    created_time=models.DateTimeField(auto_now_add=True, verbose_name="Created Time")
    updated_time=models.DateTimeField(auto_now=True, verbose_name="Updated Time") 
 

#This class is for displaying the names of the space in admin panel and database.
    class Meta:
        db_table='resource_table' # This name is used for db_table name
        verbose_name_plural="Resource" #This name is used for Admin Panel dashboard
        verbose_name="Resource" #This name is used for Admin Panel messages

#This function is for displaying the title of the spaces in admin panel.
    def __str__(self):
        return str(self.resourcename)