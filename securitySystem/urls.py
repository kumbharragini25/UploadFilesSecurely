from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    # path('admin/', admin.site.urls),
    path('',include('authentication.urls')),
    # path('owner/',include('django.contrib.auth.urls')),
    # path('owner/',include('owner.urls')),
    # path('manager/',include('django.contrib.auth.urls')),
    # path('manager/',include('manager.urls')),
    # path('users/',include('django.contrib.auth.urls')),
    # path('users/',include('users.urls')),
]