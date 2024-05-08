from django.contrib import admin


from owner.models import Owner

class OwnerAdmin(admin.ModelAdmin):
    list_display=('id','Username','Password','Confirm_password','Email','Role')


admin.site.register(Owner,OwnerAdmin)
