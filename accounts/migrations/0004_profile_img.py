# Generated by Django 4.2.3 on 2023-08-17 04:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_profile_department_alter_profile_grade_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='accounts/profile/%Y%m%d'),
        ),
    ]
