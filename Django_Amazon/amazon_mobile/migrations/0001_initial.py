# Generated by Django 3.1.7 on 2021-05-16 13:32

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Amazon_Mobile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mobile_name', models.CharField(max_length=100)),
                ('mobile_technology', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=200), blank=True, size=None)),
            ],
        ),
        migrations.CreateModel(
            name='Mobile_Technology',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('technology_name', models.CharField(max_length=200)),
            ],
        ),
    ]
