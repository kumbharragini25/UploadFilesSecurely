from django.db import models
from django.contrib.auth.models import User, Group
from django.utils import timezone
from upload.models import UploadedDocument

class SharedDocument(models.Model):
    id=models.AutoField(primary_key=True)
    document = models.ForeignKey(UploadedDocument, on_delete=models.CASCADE)
    shared_with_user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    shared_with_group = models.ForeignKey(Group, on_delete=models.CASCADE, null=True, blank=True)
    shared_at = models.DateTimeField(default=timezone.now)
    access_level = models.CharField(max_length=20, choices=[('delete', 'Delete'), ('edit', 'Edit'), ('download', 'Download')])

    class Meta:
        unique_together = ('document', 'shared_with_user', 'shared_with_group') 