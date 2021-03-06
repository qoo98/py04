# Generated by Django 4.0 on 2022-02-01 10:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('users', '0002_alter_profiles_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profiles',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to='auth.user'),
        ),
    ]
