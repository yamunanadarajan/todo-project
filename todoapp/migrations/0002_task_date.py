# Generated by Django 5.0.4 on 2024-05-06 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='date',
            field=models.DateField(default='2001-02-28'),
            preserve_default=False,
        ),
    ]
