from django.contrib import admin
from .models import UploadedEncryptedDocument

class UploadedEncryptedDocumentAdmin(admin.ModelAdmin):
    list_display = ('encrypted_file','encrypted_file')  
   
    

admin.site.register(UploadedEncryptedDocument, UploadedEncryptedDocumentAdmin) 