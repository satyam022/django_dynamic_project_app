# Generated by Django 4.1 on 2022-08-20 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='contactEnquiry',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=60)),
                ('phone', models.CharField(max_length=50)),
                ('subject', models.TextField(max_length=100)),
                ('message', models.TextField()),
            ],
        ),
    ]