# Generated by Django 3.0.5 on 2020-09-08 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('umm', '0004_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='phone',
            name='image_url',
            field=models.CharField(default=1, max_length=5000),
            preserve_default=False,
        ),
    ]