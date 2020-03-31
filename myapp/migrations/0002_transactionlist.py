# Generated by Django 3.0.3 on 2020-03-31 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TransactionList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('provider_name', models.CharField(max_length=100)),
                ('receiver_name', models.CharField(max_length=100)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=5)),
                ('paid', models.DecimalField(decimal_places=2, max_digits=5)),
                ('due', models.DecimalField(decimal_places=2, max_digits=5)),
                ('date', models.DateField()),
            ],
            options={
                'db_table': 'TransactionList',
            },
        ),
    ]
