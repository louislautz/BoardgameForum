# Generated by Django 4.0 on 2021-12-15 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_rent_return_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rent',
            name='return_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
