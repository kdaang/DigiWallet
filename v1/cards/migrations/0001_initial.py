# Generated by Django 2.2.7 on 2019-11-18 00:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('card_id', models.BigAutoField(primary_key=True, serialize=False, unique=True)),
                ('is_enabled', models.BooleanField()),
            ],
        ),
    ]
