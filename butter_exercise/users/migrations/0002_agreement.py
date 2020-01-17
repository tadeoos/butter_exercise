# Generated by Django 2.2.9 on 2020-01-17 20:49

from django.conf import settings
import django.contrib.postgres.fields.jsonb
import django.core.serializers.json
from django.db import migrations, models
import django.db.models.deletion
import butter_exercise.users.choices


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Agreement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('terms_and_services', 'Terms and Services')], default=butter_exercise.users.choices.AgreementCategories('terms_and_services'), max_length=255)),
                ('date', models.DateField(help_text='The date agreement was signed')),
                ('data', django.contrib.postgres.fields.jsonb.JSONField(encoder=django.core.serializers.json.DjangoJSONEncoder, help_text='Data agreement was signed with')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]