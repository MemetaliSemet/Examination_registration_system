# Generated by Django 2.0.4 on 2018-05-12 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cet46', '0005_auto_20180512_1435'),
    ]

    operations = [
        migrations.AlterField(
            model_name='img',
            name='img',
            field=models.ImageField(upload_to='static/images'),
        ),
    ]
