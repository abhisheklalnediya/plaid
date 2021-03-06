# Generated by Django 2.2.1 on 2019-05-22 09:36

import django.contrib.postgres.fields
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HookCalls',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', django.contrib.postgres.fields.jsonb.JSONField()),
                ('actionsTaken', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=80), size=None)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
