# Generated by Django 2.0.6 on 2018-07-04 22:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('challenges', '0015_auto_20180704_2224'),
    ]

    operations = [
        migrations.CreateModel(
            name='GameStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status_date', models.DateTimeField(auto_now_add=True)),
                ('current', models.BooleanField(default=False)),
                ('monster_score', models.IntegerField()),
            ],
            options={
                'verbose_name_plural': 'Game statuses',
            },
        ),
        migrations.AlterModelOptions(
            name='runningchallenges',
            options={'verbose_name_plural': 'Running Challenges'},
        ),
    ]
