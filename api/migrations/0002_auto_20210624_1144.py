# Generated by Django 3.1.6 on 2021-06-24 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='hosted',
            field=models.URLField(blank=True, null=True),
        ),
    ]