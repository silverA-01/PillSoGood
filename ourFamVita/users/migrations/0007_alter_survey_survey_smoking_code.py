# Generated by Django 3.2.25 on 2024-06-18 03:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_user_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='survey',
            name='survey_smoking_code',
            field=models.CharField(blank=True, max_length=10),
        ),
    ]
