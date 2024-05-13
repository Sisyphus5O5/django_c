# Generated by Django 5.0.3 on 2024-05-06 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Music',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('year', models.IntegerField(max_length=4)),
                ('singer', models.CharField(max_length=100)),
                ('genres', models.CharField(max_length=20)),
                ('lyric', models.TextField()),
            ],
        ),
    ]
