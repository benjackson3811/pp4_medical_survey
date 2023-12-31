# Generated by Django 3.2.20 on 2023-07-29 18:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('appointments', '0006_auto_20230721_1032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='appointment_number', to=settings.AUTH_USER_MODEL),
        ),
    ]
