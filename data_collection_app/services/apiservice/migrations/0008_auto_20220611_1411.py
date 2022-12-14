# Generated by Django 3.2.4 on 2022-06-11 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apiservice', '0007_annotations_part'),
    ]

    operations = [
        migrations.RenameField(
            model_name='annotations',
            old_name='Part',
            new_name='PartObject',
        ),
        migrations.AlterField(
            model_name='annotations',
            name='Color',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='annotations',
            name='Shape',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='annotations',
            name='WorkerId',
            field=models.CharField(max_length=300, null=True),
        ),
    ]
