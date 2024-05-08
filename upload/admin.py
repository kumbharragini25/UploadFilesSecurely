from django.contrib import admin
from .models import UploadedDocument

class UploadAdmin(admin.ModelAdmin):
    list_display = ('id','owner', 'name', 'file','uploaded_at','shared_with_user','shared_with_group','shared_at','access_level')  
   
    

admin.site.register(UploadedDocument, UploadAdmin)