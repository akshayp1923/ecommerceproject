# Generated by Django 4.2 on 2023-06-29 17:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='products',
            new_name='product',
        ),
    ]
