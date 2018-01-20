from django.db import models


class Service(models.Model):

    type = models.CharField(max_length=255)
    version = models.CharField(max_length=255, blank=True, null=True)

