# Generated by Django 2.1.3 on 2018-11-21 23:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aluno', '0004_auto_20181121_0815'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registroeletiva',
            name='data',
            field=models.DateTimeField(default=datetime.datetime(2018, 11, 21, 21, 28, 35, 577294), verbose_name='Data de criação'),
        ),
    ]
