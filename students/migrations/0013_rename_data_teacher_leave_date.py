# Generated by Django 5.0.3 on 2024-04-21 16:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0012_teacher_leave'),
    ]

    operations = [
        migrations.RenameField(
            model_name='teacher_leave',
            old_name='data',
            new_name='date',
        ),
    ]
