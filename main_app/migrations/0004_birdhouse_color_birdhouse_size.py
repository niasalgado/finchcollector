# Generated by Django 4.2.1 on 2023-06-05 01:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_birdhouse_alter_feeding_options_finch_birdhouses'),
    ]

    operations = [
        migrations.AddField(
            model_name='birdhouse',
            name='color',
            field=models.CharField(default='red', max_length=50),
        ),
        migrations.AddField(
            model_name='birdhouse',
            name='size',
            field=models.CharField(default='medium', max_length=50),
        ),
    ]