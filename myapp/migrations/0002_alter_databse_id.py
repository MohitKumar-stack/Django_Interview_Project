# Generated by Django 3.2.9 on 2021-11-26 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='databse',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
