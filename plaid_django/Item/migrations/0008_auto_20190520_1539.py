# Generated by Django 2.2.1 on 2019-05-20 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Item', '0007_auto_20190520_1538'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='unofficial_currency_code',
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
    ]
