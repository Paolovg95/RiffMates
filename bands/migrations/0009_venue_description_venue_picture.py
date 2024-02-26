# Generated by Django 4.2.7 on 2024-02-18 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bands', '0008_rename_venues_profiles_userprofile_venue_profiles'),
    ]

    operations = [
        migrations.AddField(
            model_name='venue',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='venue',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]