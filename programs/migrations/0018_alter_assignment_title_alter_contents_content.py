# Generated by Django 4.2.3 on 2023-08-18 23:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('programs', '0017_remove_program_user_map_progress'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignment',
            name='title',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='contents',
            name='content',
            field=models.FileField(blank=True, null=True, upload_to='programs/contents/%Y%m%d'),
        ),
    ]