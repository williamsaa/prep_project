# Generated by Django 4.2.1 on 2023-07-04 14:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('prep_app', '0014_sti_treatment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='riskhistory',
            name='imported',
        ),
        migrations.RemoveField(
            model_name='riskhistory',
            name='legacy_id',
        ),
    ]