# Generated by Django 3.2.9 on 2022-03-12 10:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0003_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='post',
            new_name='detil',
        ),
    ]
