# Generated by Django 3.2.25 on 2024-04-27 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0014_auto_20240427_1335'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_id',
            field=models.AutoField(db_column='user_id', primary_key=True, serialize=False),
        ),
    ]
