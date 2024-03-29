# Generated by Django 4.2.7 on 2024-02-29 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('promoters', '0006_promoter_street_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='promoter',
            name='city',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='promoter',
            name='country',
            field=models.CharField(default='', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='promoter',
            name='state',
            field=models.CharField(default='', max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='promoter',
            name='zip_code',
            field=models.CharField(default='',
            max_length=30),
            preserve_default=False,
        ),
    ]
