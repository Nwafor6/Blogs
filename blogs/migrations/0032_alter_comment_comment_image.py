# Generated by Django 3.2.9 on 2022-04-07 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0031_alter_comment_comment_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='comment_image',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]