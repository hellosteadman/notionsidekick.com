# Generated by Django 5.1.2 on 2024-10-30 23:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Block',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_id', models.PositiveIntegerField()),
                ('notion_id', models.UUIDField(editable=False, unique=True, verbose_name='Notion ID')),
                ('ordering', models.PositiveIntegerField(default=0)),
                ('type', models.CharField(max_length=300)),
                ('properties', models.JSONField(blank=True, default=dict)),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype')),
            ],
            options={
                'ordering': ('ordering',),
            },
        ),
    ]
