# Generated by Django 4.2.1 on 2023-07-26 21:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prep_app', '0024_alter_sexualhistory_last_sexual_encounter_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sexualhistory',
            name='gender_last_sex_partner',
            field=models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female'), ('Both', 'Both'), ('Other', 'Other')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='sexualhistory',
            name='gender_of_sex_partners_past_12months',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Both', 'Both'), ('Other', 'Other')], max_length=30),
        ),
        migrations.AlterField(
            model_name='sexualhistory',
            name='hiv_status_sex_partner',
            field=models.CharField(blank=True, choices=[('Positive', 'Positive'), ('Negative', 'Negative'), ('Unknown', 'Unknown')], max_length=30, null=True),
        ),
    ]