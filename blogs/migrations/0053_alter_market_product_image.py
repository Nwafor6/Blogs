# Generated by Django 3.2.9 on 2022-04-24 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0052_delete_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='market',
            name='product_image',
            field=models.FileField(blank=True, default='default-img.png', null=True, upload_to='comment-img/'),
        ),
    ]