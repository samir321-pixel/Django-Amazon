# Generated by Django 3.1.7 on 2021-04-05 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('amazon_admin', '0003_auto_20210402_2156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='amazon_admin',
            name='password',
            field=models.CharField(blank=True, editable=False, max_length=300, null=True, unique=True),
        ),
    ]