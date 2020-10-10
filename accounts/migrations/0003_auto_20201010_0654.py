# Generated by Django 3.1 on 2020-10-10 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_customuser_profile_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='profile_image',
        ),
        migrations.AddField(
            model_name='customuser',
            name='user_image',
            field=models.ImageField(blank=True, null=True, upload_to='profile_pics'),
        ),
    ]
