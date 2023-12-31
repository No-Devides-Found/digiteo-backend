# Generated by Django 4.2.3 on 2023-08-10 17:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_qna_qna_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='qna_image',
            old_name='qna_id',
            new_name='qna',
        ),
        migrations.CreateModel(
            name='TargetPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('target_post_type', models.CharField(default='', max_length=10)),
                ('practice', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='posts.practice')),
                ('qna', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='posts.qna')),
            ],
        ),
    ]
