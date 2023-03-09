from django.views.generic.edit import FormView
from django.views.decorators.csrf import csrf_exempt
from django.http.request import HttpRequest
from django.http.response import *
from django.shortcuts import render
from .forms import FileFieldForm
from .utils import MergeFiles
from .models import PDFFile

def downloadFile(request: HttpRequest, id : int):
    try:
        item : PDFFile = PDFFile.objects.get(upload_id = id)
    except PDFFile.DoesNotExist as e:
        raise Http404("Given url does not exits")
    return render(request, 'download.html',{'name': item})

def index(req: HttpRequest):
    return render(req,'index.html');

class MergeForm(FormView):
    form_class = FileFieldForm
    template_name = 'upload.html'  # Replace with your template.
    success_url = '/download/'  # Replace with your URL or reverse().

    def post(self, request:HttpRequest, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        files = request.FILES.getlist('file_field')
        print(str(request))
        if form.is_valid():
            name = MergeFiles(files)
            self.success_url = '/download/' + str(name.upload_id)
            return self.form_valid(form)
        else:
            return self.form_invalid(form)