# Generated by Django 5.1.1 on 2024-09-09 12:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='tickets_ouverts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='utilisateurs',
            fields=[
                ('nom', models.CharField(max_length=100)),
                ('prenom', models.CharField(max_length=100)),
                ('date', models.DateTimeField(default=datetime.datetime.now)),
                ('numero_employe', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
    ]
