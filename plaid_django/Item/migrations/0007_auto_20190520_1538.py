# Generated by Django 2.2.1 on 2019-05-20 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Item', '0006_auto_20190520_1537'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='pending_transaction_id',
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
    ]
