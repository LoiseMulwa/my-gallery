# Generated by Django 4.0.4 on 2022-05-31 12:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0002_alter_photo_category'),
    ]

    operations = [
        migrations.RenameField(
            model_name='photo',
            old_name='image',
            new_name='photo',
        ),
    ]