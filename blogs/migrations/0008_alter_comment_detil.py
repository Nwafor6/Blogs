# Generated by Django 3.2.9 on 2022-03-26 02:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0007_auto_20220323_0231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='detil',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blogs.article'),
        ),
    ]
