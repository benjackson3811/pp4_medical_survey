# Generated by Django 3.2.20 on 2023-07-19 18:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('appointments', '0003_auto_20230719_1807'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='patient_ID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='full_name', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='comments',
            name='patient_ID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='appointment_number', to=settings.AUTH_USER_MODEL),
        ),
    ]
