# Generated by Django 3.0.5 on 2020-04-20 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_auto_20200420_2118'),
    ]

    operations = [
        migrations.RenameField(
            model_name='news',
            old_name='pic',
            new_name='picname',
        ),
        migrations.AddField(
            model_name='news',
            name='picurl',
            field=models.TextField(default='-'),
        ),
    ]
