# Generated by Django 3.0.5 on 2020-05-18 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plan', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plan_section',
            name='section',
            field=models.IntegerField(verbose_name='小节号'),
        ),
    ]