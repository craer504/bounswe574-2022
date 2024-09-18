from django.db import models
from django.contrib.auth.models import User
from space.models import SpaceModel
from ckeditor.fields import RichTextField

class TermModel(models.Model):
    termwriter=models.ForeignKey(User, on_delete=models.CASCADE,related_name="term")
    termspace=models.ForeignKey(SpaceModel, on_delete=models.CASCADE, related_name="terms", blank=True)
    termtitle=models.CharField(max_length=50, blank=False, null=False)
    termdefinition=RichTextField(max_length=500, blank=False, null=False)
    termstep=models.TextField()    
    created_time=models.DateTimeField(auto_now_add=True, verbose_name="Created Time")
    updated_time=models.DateTimeField(auto_now=True, verbose_name="Updated Time")
 

#This class is for displaying the names of the space in admin panel and database.
    class Meta:
        db_table='term_table' # This name is used for db_table name
        verbose_name_plural="Terms" #This name is used for Admin Panel dashboard
        verbose_name="Term" #This name is used for Admin Panel messages

#This function is for displaying the title of the spaces in admin panel.
    def __str__(self):
        return str(self.termtitle)