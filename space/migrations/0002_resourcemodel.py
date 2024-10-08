# Generated by Django 4.1.3 on 2022-12-03 19:23

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('space', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ResourceModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resourcename', models.CharField(max_length=50)),
                ('resourceinfo', ckeditor.fields.RichTextField(blank=True, max_length=500, null=True)),
                ('resourceattachment', models.FileField(blank=True, null=True, upload_to='files_resource')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='Created Time')),
                ('updated_time', models.DateTimeField(auto_now=True, verbose_name='Updated Time')),
                ('resourcecreator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='resource', to=settings.AUTH_USER_MODEL)),
                ('resourcespace', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='resources', to='space.spacemodel')),
            ],
            options={
                'verbose_name': 'Resource',
                'verbose_name_plural': 'Resource',
                'db_table': 'resource_table',
            },
        ),
    ]
