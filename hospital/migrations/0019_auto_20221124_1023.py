# Generated by Django 3.0.5 on 2022-11-24 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0018_auto_20201015_2036'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='appointmentDate',
            field=models.DateField(),
        ),
    ]
