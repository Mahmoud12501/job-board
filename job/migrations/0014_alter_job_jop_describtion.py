# Generated by Django 4.1 on 2022-09-07 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0013_job_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='jop_describtion',
            field=models.TextField(max_length=4000),
        ),
    ]