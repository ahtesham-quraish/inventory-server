# Generated by Django 2.2 on 2019-08-10 11:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('customer', '0001_initial'),
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(blank=True, default='', max_length=20, null=True)),
                ('type', models.CharField(blank=True, default='', max_length=20, null=True)),
                ('description', models.CharField(blank=True, default='', max_length=20, null=True)),
                ('amount', models.CharField(blank=True, default='', max_length=20, null=True)),
                ('bank_account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.Bank')),
                ('category', models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, related_name='items', to='account.Category')),
                ('customer', models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='customer.Customer')),
            ],
        ),
    ]
