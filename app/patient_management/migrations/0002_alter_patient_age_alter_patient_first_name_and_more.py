# Generated by Django 5.0.1 on 2024-04-01 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient_management', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='age',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='patient',
            name='first_name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='patient',
            name='gender',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='patient',
            name='last_name',
            field=models.CharField(max_length=255),
        ),
    ]
