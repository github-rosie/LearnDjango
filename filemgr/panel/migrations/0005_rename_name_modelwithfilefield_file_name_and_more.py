# Generated by Django 5.0.7 on 2024-07-31 05:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('panel', '0004_alter_modelwithfilefield_name_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='modelwithfilefield',
            old_name='name',
            new_name='file_name',
        ),
        migrations.RenameField(
            model_name='modelwithimagefield',
            old_name='name',
            new_name='image_name',
        ),
    ]
