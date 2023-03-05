from django.db import models
import os

class PDFFile(models.Model):
    upload_id = models.AutoField(primary_key=True)
    upload = models.FileField(upload_to ='uploads/pdf/')
    def delete(self):
        if os.path.exists(self.upload.path):
            os.remove(self.upload.path)
        super().delete()

