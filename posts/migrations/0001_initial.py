# Generated by Django 2.2.3 on 2019-08-01 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('em', models.EmailField(max_length=254, unique=True)),
                ('psw', models.CharField(max_length=100)),
                ('fist_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('bio', models.TextField(blank=True)),
                ('birthdat', models.DateField(blank=True, null=True)),
                ('created', models.DateField(auto_now_add=True)),
                ('modified', models.DateField(auto_now=True)),
            ],
        ),
    ]
