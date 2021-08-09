# Generated by Django 3.2.6 on 2021-08-09 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('levelupapi', '0003_auto_20210803_2001'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='attendees',
            field=models.ManyToManyField(related_name='attending', through='levelupapi.GamerEvent', to='levelupapi.Gamer'),
        ),
    ]