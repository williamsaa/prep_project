# Generated by Django 4.2.1 on 2023-06-28 19:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('prep_app', '0005_rename_facility_id_address_facility_temp_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='address',
            name='facility_temp',
        ),
        migrations.RemoveField(
            model_name='arvmedication',
            name='facility_temp',
        ),
        migrations.RemoveField(
            model_name='cd4count',
            name='facility_temp',
        ),
        migrations.RemoveField(
            model_name='client',
            name='facility_temp',
        ),
        migrations.RemoveField(
            model_name='docket',
            name='facility_temp',
        ),
        migrations.RemoveField(
            model_name='emergencycontact',
            name='facility_temp',
        ),
        migrations.RemoveField(
            model_name='facility',
            name='facility_temp',
        ),
        migrations.RemoveField(
            model_name='organization',
            name='facility_temp',
        ),
        migrations.RemoveField(
            model_name='otherlab',
            name='facility_temp',
        ),
        migrations.RemoveField(
            model_name='parish',
            name='facility_temp',
        ),
        migrations.RemoveField(
            model_name='physicalexam',
            name='facility_temp',
        ),
        migrations.RemoveField(
            model_name='prepstatusdetail',
            name='facility_temp',
        ),
        migrations.RemoveField(
            model_name='regimen',
            name='facility_temp',
        ),
        migrations.RemoveField(
            model_name='regimenlinecode',
            name='facility_temp',
        ),
        migrations.RemoveField(
            model_name='userfacilityassignment',
            name='facility_temp',
        ),
        migrations.RemoveField(
            model_name='viralload',
            name='facility_temp',
        ),
    ]