# Generated by Django 4.2.7 on 2024-02-29 22:21

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('promoters', '0009_alter_promoter_zip_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='promoter',
            name='address',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]