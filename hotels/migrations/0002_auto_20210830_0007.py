# Generated by Django 3.2.2 on 2021-08-29 19:07

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hotels', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='rooms',
            name='room_img',
            field=models.ImageField(default='default.jpg', upload_to='images/'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='description_list',
            name='room',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='description', to='hotels.rooms'),
        ),
        migrations.AlterField(
            model_name='guests',
            name='date_from',
            field=models.DateTimeField(default=datetime.date(2021, 8, 30)),
        ),
        migrations.AlterField(
            model_name='guests',
            name='date_to',
            field=models.DateTimeField(default=datetime.date(2021, 8, 31)),
        ),
        migrations.AlterField(
            model_name='hotels',
            name='date',
            field=models.DateField(default=datetime.date(2021, 8, 30)),
        ),
    ]
