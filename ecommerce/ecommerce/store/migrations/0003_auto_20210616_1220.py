# Generated by Django 3.2.4 on 2021-06-16 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_auto_20210616_1133'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
        migrations.AddField(
            model_name='product',
            name='brand',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
