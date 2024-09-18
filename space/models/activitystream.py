from django.db import models

class ActivityStreamModel(models.Model):
    activity = models.JSONField()