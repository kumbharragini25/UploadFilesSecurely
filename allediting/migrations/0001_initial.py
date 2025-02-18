# Generated by Django 4.2.5 on 2024-05-07 15:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('upload', '0003_remove_uploadeddocument_key_userfiledata'),
        ('auth', '0012_alter_user_first_name_max_length'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='SharedDocument',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('shared_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('access_level', models.CharField(choices=[('delete', 'Delete'), ('edit', 'Edit'), ('download', 'Download')], max_length=20)),
                ('document', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='upload.uploadeddocument')),
                ('shared_with_group', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='auth.group')),
                ('shared_with_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('document', 'shared_with_user', 'shared_with_group')},
            },
        ),
    ]
