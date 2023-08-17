# Generated by Django 4.2.3 on 2023-08-18 02:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0018_alter_comment_target_post_alter_targetpost_agora_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='targetpost',
            name='agora',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='posts.agora'),
        ),
        migrations.AlterField(
            model_name='targetpost',
            name='practice',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='posts.practice'),
        ),
        migrations.AlterField(
            model_name='targetpost',
            name='qna',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='posts.qna'),
        ),
        migrations.AlterField(
            model_name='targetpost',
            name='tip',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='posts.tip'),
        ),
    ]