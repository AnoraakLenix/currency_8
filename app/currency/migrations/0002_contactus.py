# Generated by Django 4.1 on 2022-08-13 02:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('currency', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email_from', models.EmailField(max_length=254)),
                ('email_to', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=90)),
                ('message', models.CharField(max_length=7777)),
            ],
        ),
    ]
