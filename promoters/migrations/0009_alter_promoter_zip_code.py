# Generated by Django 4.2.7 on 2024-02-29 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('promoters', '0008_alter_promoter_zip_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='promoter',
            name='zip_code',
            field=models.CharField(default=0, max_length=30),
            preserve_default=False,
        ),
    ]
