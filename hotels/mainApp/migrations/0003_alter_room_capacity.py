# Generated by Django 5.0.3 on 2024-04-12 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0002_room_hotel_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='capacity',
            field=models.TextField(),
        ),
    ]
