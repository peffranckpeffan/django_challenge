# Generated by Django 3.1.7 on 2021-03-10 20:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0007_auto_20210310_2007'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='BookStatus',
            new_name='Status',
        ),
    ]
