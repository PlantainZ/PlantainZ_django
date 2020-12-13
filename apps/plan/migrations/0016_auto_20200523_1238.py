# Generated by Django 3.0.5 on 2020-05-23 04:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plan', '0015_auto_20200523_1237'),
    ]

    operations = [
        migrations.CreateModel(
            name='plan_comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField(verbose_name='用户id')),
                ('date', models.DateField(verbose_name='日期')),
                ('plan_id', models.IntegerField(verbose_name='项目id')),
                ('finish_cpt', models.IntegerField(null=True, verbose_name='章')),
                ('finish_sct', models.IntegerField(null=True, verbose_name='节')),
                ('today_comment', models.TextField(null=True, verbose_name='评注')),
            ],
            options={
                'verbose_name': '计划完成记录',
                'verbose_name_plural': '计划完成记录',
                'db_table': 'plan_comment',
            },
        ),
        migrations.DeleteModel(
            name='plan_finish',
        ),
    ]
