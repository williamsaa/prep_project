# Generated by Django 4.2.1 on 2023-07-06 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prep_app', '0017_riskassessment_performed_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='current_gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Trans: M to F', 'Trans: M to F'), ('Trans: F to M', 'Trans: F to M')], max_length=255, null=True),
        ),
    ]
