# Generated by Django 3.2.4 on 2021-06-16 00:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_auto_20210615_1633'),
    ]

    operations = [
        migrations.RenameField(
            model_name='author',
            old_name='nacionality',
            new_name='nationality',
        ),
        migrations.AlterField(
            model_name='author',
            name='genere',
            field=models.CharField(max_length=15),
        ),
    ]
