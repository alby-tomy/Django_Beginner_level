# Generated by Django 5.0 on 2023-12-14 20:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movieApp', '0003_movie_img'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movie',
            old_name='img',
            new_name='image',
        ),
    ]
