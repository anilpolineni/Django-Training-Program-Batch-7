# Generated by Django 3.0.8 on 2020-10-17 03:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FirstApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movies',
            name='director',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='movies',
            name='heroinname',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='movies',
            name='heroname',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='movies',
            name='moviename',
            field=models.CharField(max_length=100),
        ),
    ]
