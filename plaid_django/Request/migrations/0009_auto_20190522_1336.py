# Generated by Django 2.2.1 on 2019-05-22 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Request', '0008_auto_20190522_1056'),
    ]

    operations = [
        migrations.AddField(
            model_name='hookcall',
            name='item_id',
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
        migrations.AddField(
            model_name='hookcall',
            name='webhook_type',
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
    ]