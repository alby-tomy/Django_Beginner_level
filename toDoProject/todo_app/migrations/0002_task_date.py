# Generated by Django 5.0 on 2023-12-15 21:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='date',
            field=models.DateField(default='2020-02-02'),
            preserve_default=False,
        ),
    ]
