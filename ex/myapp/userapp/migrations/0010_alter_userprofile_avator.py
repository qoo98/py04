# Generated by Django 4.0 on 2022-01-23 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0009_remove_shop_avator_userprofile_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='avator',
            field=models.ImageField(default='default.png', upload_to='images/', verbose_name='avator'),
        ),
    ]
