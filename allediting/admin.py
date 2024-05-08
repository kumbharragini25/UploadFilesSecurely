from django.contrib import admin
from .models import SharedDocument

class SharedAdmin(admin.ModelAdmin):
    list_display = ('id','document', 'shared_with_user', 'shared_with_group','shared_at','access_level')  
   
    

admin.site.register(SharedDocument, SharedAdmin) 