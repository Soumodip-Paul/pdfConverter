from django.utils.timezone import now
from PyPDF2 import PdfWriter
from os.path import join
from .models import PDFFile
import re,os

def MergeFiles(files:list) -> PDFFile:
    merger = PdfWriter()
    for f in files:
        merger.append(f)
    path_file = join('media','uploads' )
    if not os.path.exists(path_file):
        os.makedirs(path_file)
    file_name = "MergedPDF-{0}.pdf".format(re.sub(r"\s+|:","-",str(now().now())[0:19]))
    output = open(join(path_file,file_name),'xb')
    merger.write(output)
    merger.close()
    output.close()
    new_file = PDFFile.objects.create()
    new_file.upload.save(file_name,open(join(path_file,file_name),'rb'),save=True)
    os.remove(join(path_file,file_name))
    return new_file