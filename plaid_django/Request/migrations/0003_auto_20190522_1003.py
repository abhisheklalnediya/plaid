# Generated by Django 2.2.1 on 2019-05-22 10:03

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Request', '0002_requests'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='HookCalls',
            new_name='HookCall',
        ),
        migrations.RenameModel(
            old_name='Requests',
            new_name='Request',
        ),
    ]
