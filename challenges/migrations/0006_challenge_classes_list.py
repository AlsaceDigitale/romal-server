# Generated by Django 2.0.6 on 2018-06-29 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('challenges', '0005_remove_runningchallenges_site'),
    ]

    operations = [
        migrations.AddField(
            model_name='challenge',
            name='classes_list',
            field=models.CharField(default='unknown', max_length=150),
            preserve_default=False,
        ),
    ]