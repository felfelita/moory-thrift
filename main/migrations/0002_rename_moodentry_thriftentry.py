# Generated by Django 5.1.1 on 2024-09-17 10:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='MoodEntry',
            new_name='ThriftEntry',
        ),
    ]
