# Generated by Django 4.2.3 on 2023-08-18 00:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0013_practice_tag_map'),
    ]

    operations = [
        migrations.AddField(
            model_name='agora',
            name='cons',
            field=models.TextField(blank=True, default='', null=True),
        ),
        migrations.AddField(
            model_name='agora',
            name='pros',
            field=models.TextField(blank=True, default='', null=True),
        ),
    ]
