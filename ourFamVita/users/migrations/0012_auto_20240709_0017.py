# Generated by Django 3.2.25 on 2024-07-09 00:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_alter_productlike_product_like_page'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredient',
            name='ingredient_caution_content',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='ingredient_function_content',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='ingredient_limit_high',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='ingredient_limit_low',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='ingredient_type',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='ingredient_unit',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
