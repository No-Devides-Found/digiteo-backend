# Generated by Django 4.2.3 on 2023-08-11 04:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_agora'),
    ]

    operations = [
        migrations.AddField(
            model_name='agora',
            name='my_opinion',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='agora',
            name='summary',
            field=models.TextField(default=''),
        ),
    ]