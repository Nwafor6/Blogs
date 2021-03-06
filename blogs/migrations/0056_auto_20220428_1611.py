# Generated by Django 3.2.9 on 2022-04-28 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0055_alter_market_product_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='roommatehelp',
            name='help_file',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='market',
            name='product_image',
            field=models.FileField(blank=True, default='default-img.png', null=True, upload_to='comment-img/'),
        ),
    ]
