# Generated by Django 4.2.3 on 2023-08-11 18:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('programs', '0008_rename_program_id_contents_program_and_more'),
        ('posts', '0007_tip_tag_map'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tip_tag_map',
            name='tag',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='programs.tag'),
        ),
    ]