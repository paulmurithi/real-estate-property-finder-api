# Generated by Django 2.2.1 on 2019-06-29 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realestate', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agent',
            name='logo',
            field=models.FileField(upload_to='logos'),
        ),
    ]
