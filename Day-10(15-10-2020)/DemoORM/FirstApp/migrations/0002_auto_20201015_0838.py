# Generated by Django 3.0.8 on 2020-10-15 03:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FirstApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='Sno',
            field=models.IntegerField(),
        ),
    ]
