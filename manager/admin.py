from django.contrib import admin

from manager.models import Managers

class ManagersAdmin(admin.ModelAdmin):
    list_display=('id','Username','Password','Confirm_password','Email','Role')


admin.site.register(Managers,ManagersAdmin)
