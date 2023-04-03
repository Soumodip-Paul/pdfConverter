from django.contrib import admin
from django.db import OperationalError
from django.http.request import HttpRequest
from .models import *
import os

try: 
    setting : Configuration = Configuration.load()
    site_name = setting.site_name
except Configuration.DoesNotExist as e:
    site_name = "PDFConverter"
except OperationalError as e:
    site_name = "PDFConverter"
except Exception as e:
    site_name = "PDFConverter"


def registerPanel(site_name) :
    admin.site.site_header = "{name} Admin Panel".format(name=site_name )
    admin.site.site_title = " {name} Admin Portal".format(name=site_name )
    admin.site.index_title = "Welcome to {name} Admin Portal".format( name=site_name )

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
    def has_add_permission(self, request: HttpRequest) -> bool:
        return False

@admin.register(Configuration)
class SettingConfig(admin.ModelAdmin):
    list_display = ['name','site_name','site_domain']
    fieldsets = (
        (None, {
            "fields" : ('site_name','site_domain', 'icon', 'apple_touch_icon')
        }),
        ("Contact Details" , {
            "fields" : ('contact_email', 'contact_number', 'address'),
            'classes': ['collapse',]
        }),
        ("Api Key", {
            "fields" : ('youtube_api_key',),
            'classes': ['collapse',]
        }),
        ("Social Links", {
            "fields" : ('instagram','github','youtube','linkedIn','twitter'),
            'classes': ['collapse',]
        }),
        ("Basic Details", {
            "fields" : ('site_description','typed_strings'),
            'classes': ['collapse',]
        }),
        ("Home page Set Up", {
            "fields" : ('welcome_text','banner','home_screen','download_screen'),
            'classes': ['collapse',]
        }),    
    )
    def save_model(self, request, obj, form, change) -> None:
        from . import config
        print(obj.icon)
        if obj.icon is None or str(obj.icon) == '':
            config.config.icon.delete()
        if obj.apple_touch_icon is None or str(obj.apple_touch_icon) == '':
            config.config.apple_touch_icon.delete()
        config.config = obj
        registerPanel(obj.site_name)
        return super().save_model(request, obj, form, change)
    def has_add_permission(self, request: HttpRequest) -> bool:
        return Configuration.objects.all().count() == 0
    def has_delete_permission(self, request: HttpRequest, obj = ...) -> bool:
        return False
    class Media:
        js = ["js/settingConfig.js"]
        css = {
            "all" : ("css/admin/config_admin.css",)
        }
