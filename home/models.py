from django.db import models
import uuid
import os
# Create your models here.

class Folder(models.Model):
    uid= models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    created_at= models.DateField(auto_now=True)

def get_upload_path(instance, filename):
    return os.path.join(str(instance.folder.uid), filename)


class File(models.Model):
    folder= models.ForeignKey(Folder, on_delete=models.CASCADE)
    file= models.FileField(upload_to=get_upload_path)
    created_at= models.DateField(auto_now=True)


    