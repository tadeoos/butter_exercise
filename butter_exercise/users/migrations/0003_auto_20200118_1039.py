# Generated by Django 2.2.9 on 2020-01-18 10:39

import butter_exercise.utils.helpers
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_agreement'),
    ]

    operations = [
        migrations.AddField(
            model_name='agreement',
            name='html',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='agreement',
            name='date',
            field=models.DateField(default=butter_exercise.utils.helpers.aware_today, help_text='The date agreement was signed'),
        ),
    ]
