# Generated by Django 3.0.5 on 2020-05-19 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plan', '0007_auto_20200519_1959'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plan_finish',
            name='date',
            field=models.DateField(verbose_name='完成日期'),
        ),
    ]