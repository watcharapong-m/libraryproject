# Generated by Django 3.1.7 on 2021-05-23 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DataProject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50)),
                ('StudentID', models.CharField(max_length=11)),
                ('ProjectName', models.CharField(max_length=255)),
                ('Advisor', models.CharField(max_length=50)),
                ('Type', models.CharField(max_length=255)),
                ('GraduationYear', models.CharField(max_length=4)),
                ('Abstract', models.TextField()),
                ('Keyword', models.CharField(max_length=255)),
                ('Technology', models.CharField(max_length=255)),
                ('Award', models.CharField(max_length=255)),
                ('LinkGit', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
