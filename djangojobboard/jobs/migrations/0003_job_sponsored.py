# Generated by Django 3.2.9 on 2021-12-28 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0002_sponsoredjobpost'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='sponsored',
            field=models.BooleanField(default=False),
        ),
    ]