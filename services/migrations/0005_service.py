# Generated by Django 5.0.4 on 2024-04-10 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0004_rename_service_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]