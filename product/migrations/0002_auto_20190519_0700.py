# Generated by Django 2.2 on 2019-05-19 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='product',
            name='quatity',
            field=models.IntegerField(default=0),
        ),
    ]