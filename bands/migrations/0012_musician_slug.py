# Generated by Django 5.0.3 on 2024-03-16 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bands', '0011_musician_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='musician',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
    ]