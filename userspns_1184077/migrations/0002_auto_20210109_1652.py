# Generated by Django 3.1.5 on 2021-01-09 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userspns_1184077', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='tanggal_lahir',
            field=models.DateField(),
        ),
    ]
