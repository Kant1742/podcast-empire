# Generated by Django 3.0.2 on 2020-02-09 16:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0012_productimage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='image',
        ),
    ]
