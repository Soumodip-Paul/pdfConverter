from django.views.generic.edit import FormView
from django.http.request import HttpRequest
from django.http.response import *
from .utils import render
from .forms import FileFieldForm, CompressFileForm,EncryptFileForm
from .utils import MergeFiles,CompressFile,EncryptFile,DecryptFile
from .models import PDFFile

def downloadFile(request: HttpRequest, id : int):
    try:
        item : PDFFile = PDFFile.objects.get(upload_id = id)
    except PDFFile.DoesNotExist as e:
        raise Http404("Given url does not exits")
    return render(request, 'download.html',{'name': item})

def index(req: HttpRequest):
    return render(req,'index.html')

def about(req:HttpRequest):
    return render(req,'about.html')

class MergeForm(FormView):
    form_class = FileFieldForm
    template_name = 'merge.html'  # Replace with your template.
    success_url = '/download/'  # Replace with your URL or reverse().

    def post(self, request:HttpRequest, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        files = request.FILES.getlist('file_field')
        # print(str(request))
        if form.is_valid():
            name = MergeFiles(files)
            self.success_url = '/download/' + str(name.upload_id)
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

class CompressForm(FormView):
    form_class = CompressFileForm
    template_name = 'compress.html'  # Replace with your template.
    success_url = '/download/'  # Replace with your URL or reverse().

    def post(self, request:HttpRequest, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        files = request.FILES.getlist('file_field')
        # print(str(request))
        if form.is_valid():
            name = CompressFile(files)
            self.success_url = '/download/' + str(name.upload_id)
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

class EncryptForm(FormView):
    form_class = EncryptFileForm
    template_name = 'encrypt.html'  # Replace with your template.
    success_url = '/download/'  # Replace with your URL or reverse().

    def post(self, request:HttpRequest, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        files = request.FILES.getlist('file_field')
        print(request.POST)
        password = request.POST.get('password')
        # print(str(request))
        if form.is_valid():
            name = EncryptFile(files,password)
            self.success_url = '/download/' + str(name.upload_id)
            return self.form_valid(form)
        else:
            return self.form_invalid(form)
        
class DecryptForm(FormView):
    form_class = EncryptFileForm
    template_name = 'decrypt.html'  # Replace with your template.
    success_url = '/download/'  # Replace with your URL or reverse().

    def post(self, request:HttpRequest, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        files = request.FILES.getlist('file_field')
        print(request.POST)
        password = request.POST.get('password')
        # print(str(request))
        if form.is_valid():
            name = DecryptFile(files,password)
            if name is not None:
                self.success_url = '/download/' + str(name.upload_id)
                return self.form_valid(form)
            else :
                form.add_error("password","Wrong Password")
                return self.form_invalid(form) 
        else:
            return self.form_invalid(form)