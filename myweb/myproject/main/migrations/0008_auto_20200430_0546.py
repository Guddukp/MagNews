# Generated by Django 3.0.5 on 2020-04-30 00:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20200325_2011'),
    ]

    operations = [
        migrations.AddField(
            model_name='main',
            name='picname',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='main',
            name='picurl',
            field=models.TextField(default=''),
        ),
    ]
