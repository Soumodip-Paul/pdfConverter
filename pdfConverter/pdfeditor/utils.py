from PyPDF2 import PdfReader,PdfWriter
from PyPDF2.errors import FileNotDecryptedError
from os.path import join
from .models import PDFFile
import os

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

def CompressFile(files:list) -> PDFFile:
    reader = PdfReader(files[0])
    merger = PdfWriter()

    for page in reader.pages:
        merger.add_page(page)
        
    for page in merger.pages:
        page.compress_content_streams()

    merger.add_metadata(reader.metadata)
    path_file = join('media','uploads' )
    path_templates = join('media','thumbnails' )
    for i in [path_file,path_templates]:
        if not os.path.exists(i):
            os.makedirs(i)
    new_file = PDFFile.objects.create()
    file_name = "Compressed-{0}.pdf".format(new_file.upload_id)#re.sub(r"\s+|:","-",str(now().now())[0:19]))
    output = open(join(path_file,file_name),'xb')
    merger.write(output)
    merger.close()
    output.close()
    new_file.upload.save(file_name,open(join(path_file,file_name),'rb'),save=True)
    os.remove(join(path_file,file_name))
    return new_file

def EncryptFile(files:list,password:str|int=123) -> PDFFile:
    reader = PdfReader(files[0])
    merger = PdfWriter()

    for page in reader.pages:
        merger.add_page(page)
        
    merger.encrypt(password)

    merger.add_metadata(reader.metadata)
    path_file = join('media','uploads' )
    path_templates = join('media','thumbnails' )
    for i in [path_file,path_templates]:
        if not os.path.exists(i):
            os.makedirs(i)
    new_file = PDFFile.objects.create()
    file_name = "Encrypted-{0}.pdf".format(new_file.upload_id)#re.sub(r"\s+|:","-",str(now().now())[0:19]))
    output = open(join(path_file,file_name),'xb')
    merger.write(output)
    merger.close()
    output.close()
    new_file.upload.save(file_name,open(join(path_file,file_name),'rb'),save=True)
    os.remove(join(path_file,file_name))
    return new_file

def DecryptFile(files:list,password:str|int=123) -> PDFFile:
    try:
        reader = PdfReader(files[0])
        merger = PdfWriter()
        if reader.is_encrypted:
            reader.decrypt(password)
        for page in reader.pages:
            merger.add_page(page)

        merger.add_metadata(reader.metadata)
        path_file = join('media','uploads' )
        path_templates = join('media','thumbnails' )
        for i in [path_file,path_templates]:
            if not os.path.exists(i):
                os.makedirs(i)
        new_file = PDFFile.objects.create()
        file_name = "Decrypted-{0}.pdf".format(new_file.upload_id)#re.sub(r"\s+|:","-",str(now().now())[0:19]))
        output = open(join(path_file,file_name),'xb')
        merger.write(output)
        merger.close()
        output.close()
        new_file.upload.save(file_name,open(join(path_file,file_name),'rb'),save=True)
        os.remove(join(path_file,file_name))
        return new_file
    except FileNotDecryptedError as e:
        print(e)
        return None
    