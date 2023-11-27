# Generated by Django 4.1.7 on 2023-05-16 10:49

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='empdomain',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('domains', models.JSONField(null=True)),
                ('last_insert', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('experience', models.FloatField()),
                ('primary_skill', models.CharField(max_length=100)),
                ('skills', models.JSONField(null=True)),
                ('rating', models.FloatField()),
                ('domains', models.CharField(max_length=100, null=True)),
                ('last_insert', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='empskill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skills', models.JSONField(null=True)),
                ('last_insert', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
