from django.contrib import admin

from users.models import Users

class UserAdmin(admin.ModelAdmin):
    list_display=('id','Username','Password','Confirm_password','Email','Role')


admin.site.register(Users,UserAdmin)


