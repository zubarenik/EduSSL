# Generated by Django 3.1.5 on 2021-01-20 22:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0003_auto_20210120_2204'),
        ('course', '0007_auto_20210120_2229'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='teachers',
            field=models.ManyToManyField(blank=True, related_name='teachers', to='teacher.Teacher'),
        ),
    ]
