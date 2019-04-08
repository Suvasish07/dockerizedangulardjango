# Generated by Django 2.1.4 on 2019-04-05 13:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('content', models.CharField(max_length=50)),
                ('created_on', models.DateField(default=datetime.date.today)),
                ('due_date', models.DateField(default=datetime.date.today)),
            ],
            options={
                'db_table': 'task',
                'ordering': ['id'],
            },
        ),
    ]
