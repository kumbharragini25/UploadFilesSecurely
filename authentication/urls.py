from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.forms),
    path('saveQuery2', views.signup, name="saveQuery2"),
    path('sin/',views.sin,name="sin"),
    path('signin/', views.signin,name="signin"),
    path('view_uploaded_files/', views.view_uploaded_files, name='view_uploaded_files'),
    path('home/', views.home),
    path('all/', views.view_all_files,name='all'),
    path('check_document_access/', views.check_document_access,name='check_document_access'),
    path('upload/',views.upload_document,name='upload'),
    path('permission/',views.permission,name="permission"),
    path('create_group/<int:document_id>/', views.create_group_for_document, name='create_group'),
    path('show_group/<int:document_id>', views.show_group, name='show_group'),
    path('share_document_with_user/<int:document_id>', views.share_document_with_user, name='share_document_with_user'),
    path('show/<int:document_id>', views.show, name='show'),
    path('edit_document/<int:document_id>/', views.edit_document, name='edit_document'),
    path('delete_document/<int:document_id>/', views.delete_document, name='delete_document'),
    path('download_document/<int:document_id>/', views.download_document, name='download_document'),
]