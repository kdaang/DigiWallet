# Generated by Django 2.2.7 on 2019-11-21 05:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stores', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='store',
            old_name='company',
            new_name='company_id',
        ),
        migrations.RemoveField(
            model_name='store',
            name='employee',
        ),
    ]
