# Generated by Django 3.1.5 on 2021-01-19 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0003_auto_20210118_2324'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='image',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='uploads.course'),
        ),
        migrations.AlterField(
            model_name='job',
            name='image',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='uploads.job'),
        ),
        migrations.AlterField(
            model_name='review',
            name='image',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='uploads.review'),
        ),
    ]
