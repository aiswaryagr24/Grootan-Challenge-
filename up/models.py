from django.db import models
from django.conf import settings
class it(models.Model):
    fil=models.FileField(upload_to='media')
    def __str__(self):
        return self.fil
    