# Generated by Django 2.0.4 on 2018-05-03 11:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cet_application',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=32)),
                ('user_id', models.CharField(max_length=18)),
                ('gender', models.BooleanField()),
                ('age', models.CharField(max_length=8)),
                ('phone', models.CharField(max_length=11)),
                ('school', models.CharField(max_length=60)),
                ('addr', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=200)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AddField(
            model_name='cet_application',
            name='topic',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cet46.Topic'),
        ),
    ]
