# Generated by Django 3.2.20 on 2023-07-19 18:07

import cloudinary.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('appointments', '0002_auto_20230719_1450'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comments',
            options={'ordering': ['-appointment_number']},
        ),
        migrations.RenameField(
            model_name='appointment',
            old_name='first_name',
            new_name='full_name',
        ),
        migrations.RenameField(
            model_name='appointment',
            old_name='Gender',
            new_name='gender',
        ),
        migrations.RenameField(
            model_name='comments',
            old_name='first_name',
            new_name='full_name',
        ),
        migrations.RenameField(
            model_name='comments',
            old_name='Gender',
            new_name='gender',
        ),
        migrations.RemoveField(
            model_name='appointment',
            name='content',
        ),
        migrations.RemoveField(
            model_name='appointment',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='appointment',
            name='referred',
        ),
        migrations.RemoveField(
            model_name='appointment',
            name='staff_member',
        ),
        migrations.RemoveField(
            model_name='comments',
            name='content',
        ),
        migrations.RemoveField(
            model_name='comments',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='comments',
            name='referred',
        ),
        migrations.RemoveField(
            model_name='comments',
            name='staff_member',
        ),
        migrations.AddField(
            model_name='appointment',
            name='address',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='appointment',
            name='appointment_notes',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='appointment',
            name='appointment_number',
            field=models.CharField(choices=[('Inital Appointment', 'Inital Appointment'), ('Follow Up Appointment', 'Follow Up Appointment'), ('Final Results', 'Final Results')], default='', max_length=50),
        ),
        migrations.AddField(
            model_name='comments',
            name='appointment_notes',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='comments',
            name='appointment_number',
            field=models.CharField(choices=[('Inital Appointment', 'Inital Appointment'), ('Follow Up Appointment', 'Follow Up Appointment'), ('Final Results', 'Final Results')], default='', max_length=50),
        ),
        migrations.AddField(
            model_name='comments',
            name='image',
            field=cloudinary.models.CloudinaryField(default='placeholder', max_length=255, verbose_name='image'),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='patient_ID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='appointment', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='status',
            field=models.IntegerField(choices=[(0, ''), (1, 'Just Recruited'), (2, 'Completed First Appointment'), (3, 'Completed Second Appointment')], default=0),
        ),
        migrations.AlterField(
            model_name='comments',
            name='patient_ID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='full_name', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='comments',
            name='status',
            field=models.IntegerField(choices=[(0, ''), (1, 'Just Recruited'), (2, 'Completed First Appointment'), (3, 'Completed Second Appointment')], default=0),
        ),
    ]
