# Generated by Django 5.1.3 on 2024-12-08 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_tasks_done'),
    ]

    operations = [
        migrations.AddField(
            model_name='proyect',
            name='done',
            field=models.BooleanField(default=False),
        ),
    ]
