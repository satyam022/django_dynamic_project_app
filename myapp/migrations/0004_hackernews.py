# Generated by Django 4.1 on 2022-08-21 07:17

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_delete_hackernews'),
    ]

    operations = [
        migrations.CreateModel(
            name='HackerNews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titles', models.CharField(max_length=100)),
                ('remark', tinymce.models.HTMLField()),
            ],
        ),
    ]
