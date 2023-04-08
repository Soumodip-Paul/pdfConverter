from django.core.exceptions import ValidationError
from django.conf import settings
def validate_file_size(value):
    
    filesize= value.size
    
    if filesize > settings.MAX_UPLOAD_SIZE:
        raise ValidationError(f"You cannot upload file more than {settings.MAX_UPLOAD_SIZE/(1024*1024)} Mb")
    else:
        return value
def validate_file_type(value):
    
    file_type= value.content_type.split('/')[1]
    
    if file_type not in settings.CONTENT_TYPES:
        raise ValidationError(f"File type not supported")
    
    return value