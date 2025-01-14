# Generated by Django 5.0.6 on 2024-06-26 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Career',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('shortname', models.CharField(max_length=10)),
                ('director', models.CharField(max_length=100)),
                ('level', models.CharField(max_length=100)),
                ('plan', models.CharField(max_length=4)),
                ('status', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('semester', models.IntegerField()),
                ('total_hours', models.IntegerField()),
                ('hours_semesters', models.IntegerField()),
                ('file', models.CharField(max_length=50)),
            ],
        ),
    ]
