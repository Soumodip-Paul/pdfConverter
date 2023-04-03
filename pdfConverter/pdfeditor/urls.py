"""pdfConverter URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from .views import *

urlpatterns = [
    path('',index,name="Index"),
    path('about',about,name="About"),
    path('merge',MergeForm.as_view(),name="Merge"),
    path('compress',CompressForm.as_view(),name="Compress"),
    path('encrypt',EncryptForm.as_view(),name="Encrypt"),
    path('decrypt',DecryptForm.as_view(),name="Decrypt"),
    path('download/<int:id>',downloadFile,name="Download")
]
