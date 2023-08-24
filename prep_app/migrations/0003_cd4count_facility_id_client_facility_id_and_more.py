# Generated by Django 4.2.1 on 2023-06-26 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prep_app', '0002_docket'),
    ]

    operations = [
        migrations.AddField(
            model_name='cd4count',
            name='facility_id',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='client',
            name='facility_id',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='emergencycontact',
            name='facility_id',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='facility',
            name='facility_id',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='organization',
            name='facility_id',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='parish',
            name='facility_id',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='physicalexam',
            name='facility_id',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='regimen',
            name='facility_id',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='regimenlinecode',
            name='facility_id',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='viralload',
            name='facility_id',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
