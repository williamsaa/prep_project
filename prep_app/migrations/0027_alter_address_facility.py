# Generated by Django 4.2.1 on 2023-08-22 21:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('prep_app', '0026_alter_client_date_of_birth'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='facility',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='prep_app.facility'),
        ),
    ]
