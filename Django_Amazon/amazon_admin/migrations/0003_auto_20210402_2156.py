# Generated by Django 3.1.7 on 2021-04-02 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('amazon_admin', '0002_amazon_admin_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='amazon_admin',
            name='password',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]