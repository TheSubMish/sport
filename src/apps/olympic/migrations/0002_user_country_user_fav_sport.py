# Generated by Django 5.0.3 on 2024-03-29 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('olympic', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='country',
            field=models.CharField(default='Nepal', max_length=255),
        ),
        migrations.AddField(
            model_name='user',
            name='fav_sport',
            field=models.CharField(default='Football', max_length=255),
        ),
    ]
