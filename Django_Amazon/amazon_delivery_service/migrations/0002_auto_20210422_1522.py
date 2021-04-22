# Generated by Django 3.1.7 on 2021-04-22 09:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('amazon_delivery_service', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='amazon_delivery_service',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='amazon_delivery_boy_notifications',
            name='amazon_delivery_boy',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='amazon_delivery_service.amazon_delivery_boy'),
        ),
        migrations.AddField(
            model_name='amazon_delivery_boy',
            name='amazon_deliery_service',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='amazon_delivery_service.amazon_delivery_service'),
        ),
        migrations.AddField(
            model_name='amazon_delivery_boy',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
