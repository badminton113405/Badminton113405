# Generated by Django 5.0.7 on 2024-10-14 04:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_remove_coursetype_schedule'),
    ]

    operations = [
        migrations.AddField(
            model_name='coursetype',
            name='additional_description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
