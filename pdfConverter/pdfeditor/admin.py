from django.contrib import admin
from .models import PDFFile
import os

# Register your models here.
@admin.register(PDFFile)
class FileAdmin(admin.ModelAdmin):
    list_display = ['upload_id','upload']
    def delete_queryset(self, request, queryset):
        print('==========================delete_queryset==========================\n')
        
        for file in queryset:
            print("delete {0} \n".format(file.upload.path))
            if os.path.exists(file.upload.path):
                os.remove(file.upload.path)
            file.delete()

        print('==========================delete_queryset==========================\n')
