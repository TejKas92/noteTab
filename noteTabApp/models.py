from django.db import models

class Note(models.Model):
    student = models.CharField(max_length=100)
    note = models.FloatField()
