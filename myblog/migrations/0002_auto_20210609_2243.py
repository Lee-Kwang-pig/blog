# Generated by Django 3.1.1 on 2021-06-09 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='author',
        ),
        migrations.AddField(
            model_name='author',
            name='name',
            field=models.CharField(default=1, max_length=20, unique=True, verbose_name='名字'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='author',
            name='sex',
            field=models.BooleanField(verbose_name='性别'),
        ),
    ]
