# Generated by Django 4.2.1 on 2023-06-28 19:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('prep_app', '0007_rename_address_facility_address1'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='facility',
            field=models.ForeignKey(default=8, on_delete=django.db.models.deletion.CASCADE, to='prep_app.facility'),
        ),
    ]
