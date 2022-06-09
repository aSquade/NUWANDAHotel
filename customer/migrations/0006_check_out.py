# Generated by Django 3.0.3 on 2020-05-11 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0005_auto_20200508_1544'),
    ]

    operations = [
        migrations.CreateModel(
            name='Check_out',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='姓名', max_length=20)),
                ('sex', models.CharField(help_text='性别', max_length=1)),
                ('id_card', models.CharField(help_text='身份证号', max_length=100)),
                ('live_room', models.CharField(help_text='入住房间', max_length=10)),
                ('deposit', models.CharField(help_text='押金是否退还', max_length=10)),
                ('damage_record', models.CharField(blank=True, default='无', help_text='损坏记录', max_length=100)),
                ('consume_record', models.CharField(blank=True, default=0, help_text='消费记录', max_length=100)),
                ('live_time', models.DateTimeField(help_text='入住时间', max_length=100)),
                ('check_out_time', models.DateTimeField(auto_now=True, help_text='退房时间')),
            ],
            options={
                'db_table': 'check_out_record',
            },
        ),
    ]
