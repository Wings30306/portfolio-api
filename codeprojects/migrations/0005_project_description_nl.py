# Generated by Django 3.0.7 on 2020-10-16 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('codeprojects', '0004_auto_20200518_1646'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='description_nl',
            field=models.TextField(default='Beschrijving binnenkort beschikbaar!'),
        ),
    ]
