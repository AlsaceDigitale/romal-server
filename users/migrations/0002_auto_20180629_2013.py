# Generated by Django 2.0.6 on 2018-06-29 20:13

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='token',
            field=models.CharField(default=uuid.UUID('07dc2b66-2ce8-4f8f-8fc2-a46a7b6d28c6'), max_length=500),
        ),
    ]
