# Generated by Django 4.1 on 2022-08-19 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0005_location_alter_job_img'),
    ]

    operations = [
        migrations.RenameField(
            model_name='location',
            old_name='name',
            new_name='city',
        ),
        migrations.AddField(
            model_name='location',
            name='countery',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
