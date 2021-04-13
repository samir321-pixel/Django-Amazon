# Generated by Django 3.1.7 on 2021-04-13 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('amazon_delivery_service', '0006_amazon_delivery_boy_notifications'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='amazon_delivery_boy',
            name='delivery_boy_name',
        ),
        migrations.AddField(
            model_name='amazon_delivery_boy',
            name='Resume',
            field=models.FileField(default='a.docs', upload_to='media/Amazon_Delivery_Boy/resume_file'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='amazon_delivery_boy',
            name='first_name',
            field=models.CharField(default='minakshi', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='amazon_delivery_boy',
            name='last_name',
            field=models.CharField(default='rout', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='amazon_delivery_boy',
            name='middle_name',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]