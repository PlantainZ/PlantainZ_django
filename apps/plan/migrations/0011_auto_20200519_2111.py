# Generated by Django 3.0.5 on 2020-05-19 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plan', '0010_auto_20200519_2109'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plan',
            name='end_time',
            field=models.DateField(verbose_name='结束时间'),
        ),
        migrations.AlterField(
            model_name='plan',
            name='start_time',
            field=models.DateField(verbose_name='开始时间'),
        ),
    ]
