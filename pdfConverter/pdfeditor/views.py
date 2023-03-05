from django.views.generic.edit import FormView
from django.views.decorators.csrf import csrf_exempt
from django.http import FileResponse
from django.http.request import HttpRequest
from .forms import FileFieldForm
from .utils import MergeFiles

class index(FormView):
    form_class = FileFieldForm
    template_name = 'upload.html'  # Replace with your template.
    success_url = '/'  # Replace with your URL or reverse().

    @csrf_exempt
    def post(self, request:HttpRequest, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        files = request.FILES.getlist('file_field')
        print(str(request))
        if form.is_valid():
            name = MergeFiles(files)
            return FileResponse(name.upload)
        else:
            return self.form_invalid(form)