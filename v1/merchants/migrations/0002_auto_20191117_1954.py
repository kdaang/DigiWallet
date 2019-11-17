# Generated by Django 2.2.7 on 2019-11-17 19:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('point_systems', '0001_initial'),
        ('merchants', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='merchant',
            name='point_system',
            field=models.ForeignKey(default=123, on_delete=django.db.models.deletion.PROTECT, to='point_systems.PointSystem'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='merchant',
            name='company_id',
            field=models.BigAutoField(primary_key=True, serialize=False, unique=True),
        ),
    ]
