# Generated by Django 3.1.7 on 2021-04-22 13:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import localflavor.in_.models
import phone_field.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Amazon_Proprietor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unique_id', models.CharField(blank=True, editable=False, max_length=200, null=True, unique=True)),
                ('first_name', models.CharField(max_length=200)),
                ('middle_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('DOB', models.DateField()),
                ('phone', phone_field.models.PhoneField(max_length=31, unique=True)),
                ('alt_phone', phone_field.models.PhoneField(max_length=31)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('Address', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=20)),
                ('state', localflavor.in_.models.INStateField(blank=True, max_length=2, null=True)),
                ('pincode', models.PositiveIntegerField(default=0)),
                ('id_proof', models.CharField(choices=[('Aadhar Card', 'Aadhar Card'), ('Pan Card', 'Pan Card')], max_length=30)),
                ('id_proof_file', models.FileField(upload_to='media/Amazon_Proprietor/id_proof_file')),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('get_notified', models.BooleanField(default=True)),
                ('password', models.CharField(blank=True, editable=False, max_length=300, null=True)),
                ('qr_code', models.ImageField(blank=True, upload_to='media/Amazon_Proprietor/qr_codes')),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]