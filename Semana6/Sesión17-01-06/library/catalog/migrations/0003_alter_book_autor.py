# Generated by Django 3.2.4 on 2021-06-15 21:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_auto_20210615_1607'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='autor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='catalog.author'),
        ),
    ]
