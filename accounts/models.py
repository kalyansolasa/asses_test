from django.conf import settings
from django.db import models
from django.utils import timezone


class FileProcess(models.Model):
    src_file_path = models.CharField(max_length=200)
    img_name = models.CharField(max_length=200)

    def publish(self):
        self.save()

    def __str__(self):
        return self.img_path


