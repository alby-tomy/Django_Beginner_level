# Generated by Django 5.0 on 2023-12-13 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieApp', '0002_movie_year'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='img',
            field=models.ImageField(default='img.img', upload_to='gallery'),
            preserve_default=False,
        ),
    ]
