# Generated by Django 5.0.3 on 2024-04-30 05:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0039_alter_customuser_profile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='profile_pic',
            field=models.ImageField(upload_to='media/profile_pic/'),
        ),
    ]
