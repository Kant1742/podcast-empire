# Generated by Django 3.0.2 on 2020-02-08 06:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0009_auto_20200207_2145'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productinorder',
            old_name='nmb',
            new_name='quantity',
        ),
    ]
