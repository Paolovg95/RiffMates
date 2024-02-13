# Generated by Django 4.2.7 on 2024-02-13 01:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('bands', '0008_rename_venues_profiles_userprofile_venue_profiles'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='SeekingAd',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seeking', models.CharField(choices=[('M', 'Musician'), ('B', 'Band')], max_length=1)),
                ('date', models.DateTimeField(auto_now=True)),
                ('content', models.TextField()),
                ('band', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='bands.band')),
                ('musician', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='bands.musician')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
