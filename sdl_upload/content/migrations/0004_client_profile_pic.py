# Generated by Django 4.1.7 on 2023-03-22 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0003_client_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]