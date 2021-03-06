# Generated by Django 4.0 on 2021-12-15 12:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('returned', models.BooleanField(default=False)),
                ('rent_time', models.DateTimeField(auto_now_add=True)),
                ('return_time', models.DateTimeField()),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.game')),
                ('renter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.user')),
            ],
        ),
    ]
