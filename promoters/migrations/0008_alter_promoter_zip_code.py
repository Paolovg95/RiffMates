# Generated by Django 4.2.7 on 2024-02-29 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('promoters', '0007_promoter_city_promoter_country_promoter_state_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='promoter',
            name='zip_code',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
