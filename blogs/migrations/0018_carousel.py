# Generated by Django 3.2.9 on 2022-04-02 22:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0017_rename_help_roommatehelp'),
    ]

    operations = [
        migrations.CreateModel(
            name='Carousel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='img')),
                ('title', models.CharField(max_length=100)),
                ('body', models.TextField()),
            ],
        ),
    ]
