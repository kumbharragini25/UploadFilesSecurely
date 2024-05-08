from django.db import models
from django.contrib.auth.models import User,Group
from django.utils import timezone

class UploadedDocument(models.Model):
    id = models.AutoField(primary_key=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    file = models.FileField(upload_to='uploaded_documents/')
    
    uploaded_at = models.DateTimeField(auto_now_add=True)
    shared_with_user = models.ForeignKey(User, related_name='shared_documents', on_delete=models.CASCADE, null=True, blank=True)
    shared_with_group = models.ForeignKey(Group, related_name='shared_documents', on_delete=models.CASCADE, null=True, blank=True)
    shared_at = models.DateTimeField(default=timezone.now)
    access_level = models.CharField(max_length=20, choices=[('delete', 'Delete'), ('edit', 'Edit'), ('download', 'Download')])

    def __str__(self):
        return self.name
    

    class UserFileData(models.Model):
       user = models.OneToOneField(User, on_delete=models.CASCADE)
       user_password = models.CharField(max_length=255)  

    def edit_document(self, new_name):
        self.name = new_name
        self.save()

    def delete_document(self):
        self.file.delete()
        self.delete()

    def __str__(self):
        return self.name