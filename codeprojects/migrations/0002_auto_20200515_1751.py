# Generated by Django 3.0.6 on 2020-05-15 17:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('codeprojects', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectLanguage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='project_languages', to='codeprojects.Language')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='project_languages', to='codeprojects.Project')),
            ],
        ),
        migrations.AddField(
            model_name='project',
            name='languages',
            field=models.ManyToManyField(related_name='projects', through='codeprojects.ProjectLanguage', to='codeprojects.Language'),
        ),
    ]
