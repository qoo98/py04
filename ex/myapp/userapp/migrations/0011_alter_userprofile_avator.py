# Generated by Django 4.0 on 2022-01-23 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0010_alter_userprofile_avator'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='avator',
            field=models.ImageField(default='default', upload_to='images/', verbose_name='avator'),
        ),
    ]