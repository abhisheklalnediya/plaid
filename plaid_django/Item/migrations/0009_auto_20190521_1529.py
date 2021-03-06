# Generated by Django 2.2.1 on 2019-05-21 15:29

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Item', '0008_auto_20190520_1539'),
    ]

    operations = [
        migrations.CreateModel(
            name='HookCalls',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', django.contrib.postgres.fields.jsonb.JSONField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AddField(
            model_name='accesstoken',
            name='itemid',
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
    ]
