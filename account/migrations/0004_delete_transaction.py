# Generated by Django 2.2 on 2019-08-09 19:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_category_title'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Transaction',
        ),
    ]