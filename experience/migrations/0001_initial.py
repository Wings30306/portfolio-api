# Generated by Django 3.0.6 on 2020-05-23 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('company_name', models.CharField(max_length=100)),
                ('company_link', models.URLField()),
                ('company_logo', models.URLField(blank=True, null=True)),
                ('type', models.CharField(choices=[('INT', 'Internship'), ('VOL', 'Volunteer'), ('TMP', 'Temporary Contract'), ('IND', 'Indefinite')], default='IND', max_length=3)),
                ('description', models.TextField()),
                ('start_date', models.DateField()),
                ('end_date', models.DateField(blank=True, null=True)),
                ('code_related', models.BooleanField()),
            ],
        ),
    ]