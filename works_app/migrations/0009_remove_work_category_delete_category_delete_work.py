# Generated by Django 4.2.4 on 2023-09-01 14:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('works_app', '0008_delete_project'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='work',
            name='category',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='Work',
        ),
    ]
