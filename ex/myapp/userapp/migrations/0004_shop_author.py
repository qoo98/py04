# Generated by Django 4.0 on 2022-01-16 03:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('userapp', '0003_remove_shop_lists_delete_lists'),
    ]

    operations = [
        migrations.AddField(
            model_name='shop',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
        ),
    ]
