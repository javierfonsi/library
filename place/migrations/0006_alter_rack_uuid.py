# Generated by Django 3.2 on 2022-05-18 22:35

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('place', '0005_alter_rack_uuid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rack',
            name='uuid',
            field=models.UUIDField(default=uuid.UUID('c02bac0e-61ba-4c9d-ba92-11fe6e7f77fe')),
        ),
    ]
