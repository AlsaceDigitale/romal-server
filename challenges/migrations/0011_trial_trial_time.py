# Generated by Django 2.0.6 on 2018-07-01 22:51

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('challenges', '0010_auto_20180701_2233'),
    ]

    operations = [
        migrations.AddField(
            model_name='trial',
            name='trial_time',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
