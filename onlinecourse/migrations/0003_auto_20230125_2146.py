# Generated by Django 3.1.3 on 2023-01-25 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onlinecourse', '0002_auto_20230125_0038'),
    ]

    operations = [
        migrations.AlterField(
            model_name='choice',
            name='is_correct',
            field=models.IntegerField(default=0),
        ),
    ]
