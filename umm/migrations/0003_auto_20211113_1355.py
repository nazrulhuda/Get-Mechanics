# Generated by Django 3.2.7 on 2021-11-13 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('umm', '0002_alter_mechanics_identity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='appointment',
            field=models.CharField(default=' ', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='license',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='phone',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]