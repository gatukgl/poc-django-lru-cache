# Generated by Django 3.1.4 on 2020-12-30 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('counter', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='counter',
            name='number',
            field=models.IntegerField(default=0),
        ),
    ]
