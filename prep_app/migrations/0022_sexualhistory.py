# Generated by Django 4.2.1 on 2023-07-26 18:12

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('prep_app', '0021_alter_riskassessment_serum_creatinine_result'),
    ]

    operations = [
        migrations.CreateModel(
            name='SexualHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('modified_on', models.DateTimeField(auto_now=True, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('last_sexual_encounter', models.DateField()),
                ('date', models.DateField()),
                ('lmp_date', models.DateField()),
                ('gender_last_sex_partner', models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], max_length=30, null=True)),
                ('no_sex_partners_last_month', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1000)])),
                ('no_sex_partners_last_3month', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5000)])),
                ('no_sex_partners_last_12month', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10000)])),
                ('gender_of_sex_partners_past_12months', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], max_length=30)),
                ('condom_use_last_3months', models.CharField(choices=[('< 1/2 the time', '< 1/2 the time'), ('> 1/2 the time', '> 1/2 the time'), ('Never', 'Never')], max_length=30)),
                ('notes', models.TextField(blank=True, null=True)),
                ('anal_insertive', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='anal_insertive_set', to='prep_app.yesnocode')),
                ('anal_receptive', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='anal_receptive_set', to='prep_app.yesnocode')),
                ('anal_sex_in_last_12_months', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='anal_sex_in_12months_set', to='prep_app.yesnocode')),
                ('circumcised', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='circumcised_set', to='prep_app.yesnocode')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='prep_app.client')),
                ('condom_use_last_anal_sex_encounter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='condom_use_last_anal_sex_set', to='prep_app.yesnocode')),
                ('condom_use_last_sex_encounter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='condom_use_last_sex_set', to='prep_app.yesnocode')),
                ('contraception', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='prep_app.contraceptivemethodcode')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='%(app_label)s_%(class)s_created_by', related_query_name='%(app_label)s_%(class)ss', to=settings.AUTH_USER_MODEL)),
                ('deleted_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='%(app_label)s_%(class)s_deleted_by', related_query_name='%(app_label)s_%(class)ss', to=settings.AUTH_USER_MODEL)),
                ('facility', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='prep_app.facility')),
                ('gender_based_violence', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='gender_violence_set', to='prep_app.yesnocode')),
                ('hiv_status_sex_partner', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='prep_app.yesnocode')),
                ('in_your_lifetime_ever_paid_for_sex', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='paid_for_sex_set', to='prep_app.yesnocode')),
                ('intimate_partner_violence', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='partner_violence_set', to='prep_app.yesnocode')),
                ('is_sex_in_exchange_for_money_a_source_of_income_for_you', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sex_for_money_income_set', to='prep_app.yesnocode')),
                ('modified_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='%(app_label)s_%(class)s_modified_by', related_query_name='%(app_label)s_%(class)ss', to=settings.AUTH_USER_MODEL)),
                ('previous_hiv_test', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='previous_hiv_test_set', to='prep_app.yesnocode')),
                ('previous_prep_use', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='previous_prep_use_set', to='prep_app.yesnocode')),
            ],
            options={
                'default_permissions': ('add', 'change', 'delete', 'view', 'list'),
            },
        ),
    ]