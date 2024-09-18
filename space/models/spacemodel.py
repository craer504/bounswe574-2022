from enum import unique
from pyexpat import model
from django.db import models
from autoslug import AutoSlugField
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

class SpaceModel(models.Model):
    author=models.ForeignKey(User, on_delete=models.CASCADE, related_name="createdSpaces", verbose_name='creator')
    title=models.CharField(max_length=50, blank=False, null=False)
    content=RichTextField()
    created_date=models.DateTimeField(auto_now_add=True, verbose_name="Created Date")
    members=models.ManyToManyField(User, related_name="includedSpaces", verbose_name='members')
    tag1=models.CharField(max_length=50, blank=True, null=True)
    wiki1=models.CharField(max_length=50, blank=True, null=True)
    tag2=models.CharField(max_length=50, blank=True, null=True)
    wiki2=models.CharField(max_length=50, blank=True, null=True)
    tag3=models.CharField(max_length=50, blank=True, null=True)
    wiki3=models.CharField(max_length=50, blank=True, null=True)
    searchwords=models.CharField(max_length=5000, blank=True, null=True)
    slug=AutoSlugField(populate_from='title', unique=True)

#This class is for displaying the names of the space in admin panel and database.
    class Meta:
        db_table='space' # This name is used for db_table name
        verbose_name_plural="Spaces" #This name is used for Admin Panel dashboard
        verbose_name="Space" #This name is used for Admin Panel messages

#This function is for displaying the title of the spaces in admin panel.
    def __str__(self):
        return str(self.title)

#This function is for displaying members of the space in the admin panel.
    def member_list(self):
        return "\n".join([p.username for p in self.members.all()])

