from django.contrib.auth.models import User
from django.db import models

class ExtendedUser(models.Model):
    extendeduser = models.OneToOneField(User, on_delete=models.CASCADE)
    interest = models.CharField(max_length=100)


    #This class is for displaying the names of the space in admin panel and database.
    class Meta:
        db_table='ExtendedUser' # This name is used for db_table name
        verbose_name_plural="extendedusers" #This name is used for Admin Panel dashboard
        verbose_name="extendeduser" #This name is used for Admin Panel messages

    #This function is for displaying the title of the spaces in admin panel.
    def __str__(self):
        return str(self.extendeduser)
