# Generated by Django 4.2.7 on 2023-11-10 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meetups', '0004_participant_meetup_participants'),
    ]

    operations = [
        migrations.AddField(
            model_name='meetup',
            name='date',
            field=models.DateField(default='2023-11-12'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='meetup',
            name='organizer_email',
            field=models.EmailField(default='darko@test.com', max_length=254),
            preserve_default=False,
        ),
    ]