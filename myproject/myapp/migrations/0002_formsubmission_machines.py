# Generated by Django 5.2.1 on 2025-05-19 22:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='formsubmission',
            name='machines',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
