# Generated by Django 4.2.3 on 2023-08-16 13:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('programs', '0012_rename_is_want_program_user_map_participate_and_more'),
        ('posts', '0010_evaluation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evaluation',
            name='program_user_map',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='programs.program_user_map'),
        ),
    ]
