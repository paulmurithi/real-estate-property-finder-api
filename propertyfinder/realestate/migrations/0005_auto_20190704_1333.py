# Generated by Django 2.2.1 on 2019-07-04 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realestate', '0004_auto_20190701_1311'),
    ]

    operations = [
        migrations.AddField(
            model_name='house',
            name='suburb',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='house',
            name='town',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
