# Generated by Django 4.1.7 on 2023-04-01 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='HomePage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('background_photo', models.ImageField(upload_to='homepage/')),
                ('content', models.TextField()),
            ],
        ),
    ]
