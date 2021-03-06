# Generated by Django 2.2.4 on 2022-05-01 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0003_auto_20220429_2013'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='article',
        ),
        migrations.RemoveField(
            model_name='text',
            name='article',
        ),
        migrations.RemoveField(
            model_name='video',
            name='article',
        ),
        migrations.AddField(
            model_name='article',
            name='file',
            field=models.FileField(blank=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='article',
            name='image',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='article',
            name='text',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='File',
        ),
        migrations.DeleteModel(
            name='Image',
        ),
        migrations.DeleteModel(
            name='Text',
        ),
        migrations.DeleteModel(
            name='Video',
        ),
    ]
