# Generated by Django 4.1.7 on 2023-03-24 07:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0007_alter_client_profile_pic'),
    ]

    operations = [
        migrations.RenameField(
            model_name='client',
            old_name='profile_pic',
            new_name='profile_document',
        ),
    ]
