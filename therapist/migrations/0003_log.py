# Generated by Django 3.1.7 on 2021-02-23 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('therapist', '0002_auto_20210222_1250'),
    ]

    operations = [
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('log_date', models.TimeField(auto_now_add=True)),
                ('description', models.TextField(default='N/A')),
            ],
        ),
    ]
