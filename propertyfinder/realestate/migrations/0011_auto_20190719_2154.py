# Generated by Django 2.1.5 on 2019-07-19 21:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('realestate', '0010_houserequest_landrequest_roomrequest'),
    ]

    operations = [
        migrations.AlterField(
            model_name='houseimage',
            name='house',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='realestate.House'),
        ),
        migrations.AlterField(
            model_name='landimage',
            name='land',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='realestate.Land'),
        ),
        migrations.AlterField(
            model_name='roomimage',
            name='Room',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='realestate.Room'),
        ),
    ]