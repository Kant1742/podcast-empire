# Generated by Django 3.0.2 on 2020-01-22 12:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='episode',
            old_name='name',
            new_name='title',
        ),
    ]
