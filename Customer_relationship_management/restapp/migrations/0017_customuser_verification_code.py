# Generated by Django 4.1.7 on 2023-06-02 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restapp', '0016_remove_comment_user_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='verification_code',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
