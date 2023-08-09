# Generated by Django 4.2.3 on 2023-08-09 04:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('programs', '0004_rename_category_category_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tags',
            old_name='tag',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='program',
            name='tag',
        ),
        migrations.CreateModel(
            name='Program_Tags_Map',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('program_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='programs.program')),
                ('tag_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='programs.tags')),
            ],
        ),
    ]