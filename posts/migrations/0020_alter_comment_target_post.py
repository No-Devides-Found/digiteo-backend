# Generated by Django 4.2.3 on 2023-08-18 03:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0019_alter_targetpost_agora_alter_targetpost_practice_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='target_post',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='posts.targetpost'),
        ),
    ]
