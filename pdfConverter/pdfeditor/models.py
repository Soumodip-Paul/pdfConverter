from django.db import models
from django.core.validators import FileExtensionValidator
try: from pdfConverter.secret import site_name as siteName, smtp_mail as contactEmail
except ImportError : siteName = 'localhost'; contactEmail = 'examle@localhost'
import os

class PDFFile(models.Model):
    upload_id = models.AutoField(primary_key=True)
    upload = models.FileField(upload_to ='uploads/pdf/')
    def __str__(self) -> str:
        return self.upload.path.split(r'/')[-1]
    def delete(self):
        if os.path.exists(self.upload.path):
            os.remove(self.upload.path)
        super().delete()

class Singleton(models.Model):
    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        self.pk = 1
        super(Singleton, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        pass

    @classmethod
    def load(cls):
        obj, _ = cls.objects.get_or_create(pk=1)
        return obj

class Configuration(Singleton):
    name = "Django Configurations"
    # Site Info
    site_name = models.CharField(default='PDFeditor',max_length=255,help_text='SITE NAME')
    site_domain = models.CharField(default=siteName,max_length=255,help_text='SITE DOMAIN NAME')
    icon = models.FileField(default='',upload_to='icon/', help_text="Select a .ico Icon File",validators=[FileExtensionValidator(['ico'])],null=True,blank=True)
    apple_touch_icon = models.FileField(default='',upload_to='icon/', help_text="Select a Apple Touch Icon File",validators=[FileExtensionValidator(['jpg', 'png', 'svg'])],null=True,blank=True)
    # Address and Contact Details
    address = models.TextField(default="",blank=True,null=True,help_text="Enter Your Full Address")
    contact_email = models.EmailField(default=contactEmail, help_text='CONTACT EMAIL ADDRESS')
    contact_number = models.CharField(default='',max_length=16,blank=True,null=True, help_text="Enter your phone number")
    # Site Description
    site_description = models.TextField(default='',blank=True,null=True)
    typed_strings = models.TextField(default="hi",blank=True,null=True,help_text="Use comma separated Typed JS string values")
    # Home Page Set Up
    welcome_text = models.CharField(default='Welcome to PDFeditor',max_length=255,help_text='Set Up your welcome title')
    home_screen = models.FileField(default='',upload_to='home/image/%Y/%m/%d', validators=[FileExtensionValidator(['jpg', 'png', 'svg'])],null=True,blank=True)
    download_screen = models.FileField(default='',upload_to='home/image/%Y/%m/%d', validators=[FileExtensionValidator(['jpg', 'png', 'svg'])],null=True,blank=True)
    banner = models.FileField(default='',upload_to='home/image/%Y/%m/%d', validators=[FileExtensionValidator(['jpg', 'png', 'svg'])],null=True,blank=True)
    # API Keys
    youtube_api_key = models.CharField(null=True,blank=True,max_length=255,help_text="Your Youtube API key")
    # Social Media Username
    instagram = models.CharField(null=True,blank=True,max_length=255,help_text="Your Instagram username")
    github = models.CharField(null=True,blank=True,max_length=255,help_text="Your Github username")
    linkedIn = models.CharField(null=True,blank=True,max_length=255,help_text="Your LinkedIn username")
    twitter = models.CharField(null=True,blank=True,max_length=255,help_text="Your Twitter username")
    youtube = models.CharField(null=True,blank=True,max_length=255,help_text="Your Youtube ChannelId")
    def __str__(self) -> str:
        return self.name
    

