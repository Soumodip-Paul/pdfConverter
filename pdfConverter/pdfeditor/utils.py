# from django.utils.timezone import now
from PyPDF2 import PdfWriter
from os.path import join
from .models import PDFFile
import os #,re

def MergeFiles(files:list) -> PDFFile:
    merger = PdfWriter()
    for f in files:
        merger.append(f)
    path_file = join('media','uploads' )
    path_templates = join('media','thumbnails' )
    for i in [path_file,path_templates]:
        if not os.path.exists(i):
            os.makedirs(i)
    new_file = PDFFile.objects.create()
    file_name = "MergedPDF-{0}.pdf".format(new_file.upload_id)#re.sub(r"\s+|:","-",str(now().now())[0:19]))
    output = open(join(path_file,file_name),'xb')
    merger.write(output)
    merger.close()
    output.close()
    new_file.upload.save(file_name,open(join(path_file,file_name),'rb'),save=True)
    os.remove(join(path_file,file_name))
    return new_file