# Generated by Django 3.0.5 on 2020-04-27 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SubCat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('catname', models.CharField(max_length=50)),
                ('catid', models.IntegerField()),
            ],
        ),
    ]
