# Generated by Django 4.2.7 on 2023-12-21 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bands', '0003_band'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='room_name',
            field=models.CharField(max_length=20, null=True),
        ),
    ]