# Generated by Django 3.2.9 on 2022-04-12 00:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blogs', '0045_delete_market'),
    ]

    operations = [
        migrations.CreateModel(
            name='Market',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('AM', 'Automobile'), ('Com', 'Computer'), ('Ph', 'Phone'), ('Others', 'Others')], max_length=10)),
                ('product_name', models.CharField(max_length=100)),
                ('product_price', models.FloatField()),
                ('post', models.DateTimeField(auto_now_add=True)),
                ('product_image', models.ImageField(blank=True, default='view.jpg', null=True, upload_to='')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
