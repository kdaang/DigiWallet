# Generated by Django 2.2.7 on 2019-11-24 21:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('transaction_id', models.BigAutoField(primary_key=True, serialize=False, unique=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('total', models.BigIntegerField()),
                ('from_user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='from_user', to=settings.AUTH_USER_MODEL)),
                ('to_user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='to_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
