# Generated by Django 5.0.4 on 2024-04-09 23:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0002_service_photourl'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='service',
            name='photoUrl',
        ),
        migrations.AddField(
            model_name='service',
            name='image_url',
            field=models.URLField(blank=True),
        ),
    ]