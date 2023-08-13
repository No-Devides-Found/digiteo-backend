# Generated by Django 4.2.3 on 2023-08-11 21:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='department',
            field=models.CharField(blank=True, default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='profile',
            name='grade',
            field=models.CharField(blank=True, default='', max_length=5),
        ),
        migrations.AlterField(
            model_name='profile',
            name='nickname',
            field=models.CharField(max_length=10),
        ),
    ]