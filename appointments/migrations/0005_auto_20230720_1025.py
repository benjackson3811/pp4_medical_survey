# Generated by Django 3.2.20 on 2023-07-20 10:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('appointments', '0004_auto_20230719_1810'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='author',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='appointment_number', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='comments',
            name='author',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='appointment_notes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='patient_ID',
            field=models.CharField(max_length=80),
        ),
        migrations.AlterField(
            model_name='comments',
            name='patient_ID',
            field=models.CharField(max_length=80),
        ),
    ]
