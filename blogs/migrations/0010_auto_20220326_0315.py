# Generated by Django 3.2.9 on 2022-03-26 02:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0009_alter_comment_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='body',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='detil',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='user',
        ),
    ]
