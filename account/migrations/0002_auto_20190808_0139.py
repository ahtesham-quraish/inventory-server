# Generated by Django 2.2 on 2019-08-08 01:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='', max_length=20, null=True)),
                ('code', models.CharField(blank=True, default='', max_length=20, null=True)),
                ('type', models.CharField(blank=True, default='', max_length=20, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='transaction',
            name='bank_account',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.Bank'),
        ),
    ]