# Generated by Django 2.2.1 on 2019-05-22 10:56

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('Request', '0007_request_rid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='request',
            name='rid',
            field=models.UUIDField(default=uuid.uuid4, editable=False, verbose_name='id'),
        ),
    ]
