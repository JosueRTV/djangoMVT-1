# Generated by Django 2.2.3 on 2019-08-06 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0006_auto_20190805_1030'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='county',
            field=models.CharField(blank=True, max_length=40),
        ),
    ]
