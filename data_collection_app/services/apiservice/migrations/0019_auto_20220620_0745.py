# Generated by Django 3.2.13 on 2022-06-20 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apiservice', '0018_images_iteration'),
    ]

    operations = [
        migrations.AddField(
            model_name='annotations',
            name='DateSubmitted',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='images',
            name='DateFetched',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
