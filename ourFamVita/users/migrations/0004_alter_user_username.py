# Generated by Django 3.2.25 on 2024-06-16 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20240615_1318'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.EmailField(max_length=50, unique=True),
        ),
    ]
