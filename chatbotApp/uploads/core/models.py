from __future__ import unicode_literals

from django.db import models


UPLOAD_PATH = "documents/%Y/%m/%d/"

class ImageUploadModel(models.Model):
    

    image = models.ImageField(blank=True, null=True, upload_to=UPLOAD_PATH)
    uploaded_at = models.DateTimeField(auto_now_add=True)