# Generated by Django 3.0.5 on 2020-09-08 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('umm', '0005_phone_image_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phone',
            name='image_url',
            field=models.CharField(max_length=2083),
        ),
    ]