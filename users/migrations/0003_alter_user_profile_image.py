# Generated by Django 4.1.2 on 2022-10-18 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_user_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profile_image',
            field=models.ImageField(default='default.png', upload_to='profile_images/'),
        ),
    ]