# Generated by Django 2.2 on 2019-05-15 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fName', models.CharField(max_length=20)),
                ('lName', models.CharField(max_length=20)),
                ('Address1', models.CharField(blank=True, default=None, max_length=300, null=True)),
                ('Address2', models.CharField(blank=True, default=None, max_length=300, null=True)),
                ('Phone', models.IntegerField(blank=True, default=None, null=True)),
                ('postal_code', models.CharField(blank=True, default=None, max_length=20, null=True)),
                ('city', models.CharField(max_length=20)),
                ('company_name', models.CharField(blank=True, default=None, max_length=20, null=True)),
                ('country', models.CharField(blank=True, default='Pakistan', max_length=20, null=True)),
                ('email', models.CharField(max_length=100)),
                ('description', models.CharField(blank=True, default=None, max_length=200, null=True)),
                ('created', models.DateTimeField(auto_now=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]