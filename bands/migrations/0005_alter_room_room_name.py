# Generated by Django 4.2.7 on 2023-12-21 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bands', '0004_alter_room_room_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='room_name',
            field=models.CharField(default='Room', max_length=20),
            preserve_default=False,
        ),
    ]
