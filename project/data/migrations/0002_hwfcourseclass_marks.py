# Generated by Django 2.0.4 on 2018-07-19 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='hwfcourseclass',
            name='marks',
            field=models.FloatField(default=0.0),
        ),
    ]
