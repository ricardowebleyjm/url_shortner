# Generated by Django 4.2.3 on 2023-07-19 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortner', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='url',
            name='shortened_url',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]
