# Generated by Django 3.2.9 on 2022-04-12 00:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0046_market'),
    ]

    operations = [
        migrations.AlterField(
            model_name='market',
            name='product_price',
            field=models.FloatField(default=10.0),
        ),
    ]
