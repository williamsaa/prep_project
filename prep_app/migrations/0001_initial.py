# Generated by Django 4.2.1 on 2023-06-23 15:57

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('modified_on', models.DateTimeField(auto_now=True, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('last_name', models.CharField(max_length=255)),
                ('first_name', models.CharField(max_length=255)),
                ('middle_name', models.CharField(blank=True, max_length=255, null=True)),
                ('pet_name', models.CharField(blank=True, max_length=255, null=True)),
                ('date_of_birth', models.DateField(default='2001-01-01')),
                ('death_date', models.DateField(blank=True, null=True)),
                ('mother_last_name', models.CharField(blank=True, max_length=255, null=True)),
                ('mother_first_name', models.CharField(blank=True, max_length=255, null=True)),
                ('father_last_name', models.CharField(blank=True, max_length=255, null=True)),
                ('father_first_name', models.CharField(blank=True, max_length=255, null=True)),
                ('nhf_card', models.CharField(blank=True, max_length=255, null=True, verbose_name='NHF Card')),
                ('trn_number', models.CharField(blank=True, max_length=255, null=True, verbose_name='TRN Number')),
                ('cause_of_death', models.CharField(blank=True, max_length=255, null=True)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='%(app_label)s_%(class)s_created_by', related_query_name='%(app_label)s_%(class)ss', to=settings.AUTH_USER_MODEL)),
                ('deleted_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='%(app_label)s_%(class)s_deleted_by', related_query_name='%(app_label)s_%(class)ss', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CommunityCode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('deactivated_at', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Facility',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('modified_on', models.DateTimeField(auto_now=True, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('name', models.CharField(max_length=255)),
                ('code', models.CharField(max_length=255, unique=True)),
                ('lab_ref_code', models.CharField(blank=True, max_length=255, null=True, verbose_name='LAB reference code')),
                ('address', models.CharField(blank=True, max_length=255, null=True)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='%(app_label)s_%(class)s_created_by', related_query_name='%(app_label)s_%(class)ss', to=settings.AUTH_USER_MODEL)),
                ('deleted_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='%(app_label)s_%(class)s_deleted_by', related_query_name='%(app_label)s_%(class)ss', to=settings.AUTH_USER_MODEL)),
                ('modified_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='%(app_label)s_%(class)s_modified_by', related_query_name='%(app_label)s_%(class)ss', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='FamilyPlanningMethodCode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('code', models.CharField(max_length=255)),
                ('deactivated_at', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='GenderCode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.IntegerField()),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='HivCategoryCode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('code', models.CharField(max_length=255)),
                ('deactivated_at', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='LabTestCode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('code', models.CharField(max_length=255)),
                ('deactivated_at', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='MammogramResultCode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('code', models.CharField(max_length=255)),
                ('deactivated_at', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='MaritalStatusCode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('code', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='MonthDurationCode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('arv_duration', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='NonTreponemalResultCode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('code', models.CharField(max_length=255)),
                ('deactivated_at', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='PapSmearResultCode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('code', models.CharField(max_length=255)),
                ('deactivated_at', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='PatientStabilityStatusCode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('code', models.CharField(max_length=255)),
                ('deactivated_at', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='PrepStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('code', models.CharField(max_length=255)),
                ('deactivated_at', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='RegionCode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('code', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='RelationshipCode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('code', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='RespiratoryRateCode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('code', models.CharField(max_length=255)),
                ('deactivated_at', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='TreponemalResultCode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('code', models.CharField(max_length=255)),
                ('deactivated_at', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='UrinalysisCode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('code', models.CharField(max_length=255)),
                ('deactivated_at', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='YesNoCode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('code', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='ViralLoad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('modified_on', models.DateTimeField(auto_now=True, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('is_viral_load_request', models.BooleanField(default=False, verbose_name='Sampling for Viral Load')),
                ('test_date', models.DateField()),
                ('test_result', models.FloatField(blank=True, null=True)),
                ('undetectable', models.BooleanField(default=False)),
                ('disa_reference_id', models.CharField(blank=True, max_length=255, null=True)),
                ('notes', models.TextField(blank=True, null=True)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='prep_app.client')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='%(app_label)s_%(class)s_created_by', related_query_name='%(app_label)s_%(class)ss', to=settings.AUTH_USER_MODEL)),
                ('deleted_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='%(app_label)s_%(class)s_deleted_by', related_query_name='%(app_label)s_%(class)ss', to=settings.AUTH_USER_MODEL)),
                ('modified_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='%(app_label)s_%(class)s_modified_by', related_query_name='%(app_label)s_%(class)ss', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'default_permissions': ('add', 'change', 'delete', 'view', 'list'),
            },
        ),
        migrations.CreateModel(
            name='RegimenLineCode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('modified_on', models.DateTimeField(auto_now=True, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('line', models.IntegerField()),
                ('name', models.CharField(max_length=255)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='%(app_label)s_%(class)s_created_by', related_query_name='%(app_label)s_%(class)ss', to=settings.AUTH_USER_MODEL)),
                ('deleted_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='%(app_label)s_%(class)s_deleted_by', related_query_name='%(app_label)s_%(class)ss', to=settings.AUTH_USER_MODEL)),
                ('modified_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='%(app_label)s_%(class)s_modified_by', related_query_name='%(app_label)s_%(class)ss', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Regimen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('modified_on', models.DateTimeField(auto_now=True, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('name', models.CharField(max_length=255)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='%(app_label)s_%(class)s_created_by', related_query_name='%(app_label)s_%(class)ss', to=settings.AUTH_USER_MODEL)),
                ('deleted_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='%(app_label)s_%(class)s_deleted_by', related_query_name='%(app_label)s_%(class)ss', to=settings.AUTH_USER_MODEL)),
                ('line', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='regimen_line', to='prep_app.regimenlinecode')),
                ('modified_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='%(app_label)s_%(class)s_modified_by', related_query_name='%(app_label)s_%(class)ss', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PrepStatusDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status_date', models.DateField()),
                ('deactivated_at', models.BooleanField(default=False)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='prep_app.client')),
                ('prepstatus', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='prep_app.prepstatus')),
            ],
        ),
        migrations.CreateModel(
            name='PhysicalExam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('modified_on', models.DateTimeField(auto_now=True, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('clinic_date', models.DateField(default=datetime.datetime.now)),
                ('examined_by', models.CharField(max_length=255)),
                ('presenting_complaints', models.TextField(blank=True, null=True)),
                ('history_of_complaints', models.TextField(blank=True, null=True)),
                ('weight', models.FloatField(blank=True, null=True)),
                ('height', models.FloatField(blank=True, null=True)),
                ('blood_pressure', models.CharField(blank=True, max_length=255, null=True)),
                ('bmi', models.FloatField(blank=True, null=True)),
                ('pap_smear_date', models.DateField(blank=True, null=True)),
                ('mammogram_date', models.DateField(blank=True, null=True)),
                ('anal_pap_smear_date', models.DateField(blank=True, null=True)),
                ('psa_date', models.DateField(blank=True, null=True)),
                ('notes', models.TextField(blank=True, null=True)),
                ('temperature', models.FloatField(blank=True, null=True)),
                ('last_menstrual_period', models.DateField(blank=True, null=True)),
                ('pregnant_edd', models.DateField(blank=True, null=True)),
                ('next_appointment_date', models.DateField(blank=True, null=True)),
                ('syphilis_treponemal_resultdate', models.DateField(blank=True, null=True)),
                ('syphilis_non_treponemal_resultdate', models.DateField(blank=True, null=True)),
                ('weight_loss', models.BooleanField(default=False)),
                ('difficulty_breathing', models.BooleanField(default=False)),
                ('cough', models.BooleanField(default=False)),
                ('skin_rash', models.BooleanField(default=False)),
                ('chect_pain', models.BooleanField(default=False)),
                ('adbominal_pain', models.BooleanField(default=False)),
                ('vomiting', models.BooleanField(default=False)),
                ('diarrhea', models.BooleanField(default=False)),
                ('dehydration', models.BooleanField(default=False)),
                ('headache', models.BooleanField(default=False)),
                ('weakness', models.BooleanField(default=False)),
                ('suicidal_thoughts', models.BooleanField(default=False)),
                ('illegal_drugs', models.BooleanField(default=False)),
                ('alcohol', models.BooleanField(default=False)),
                ('using_family_planning', models.BooleanField(default=False)),
                ('anal_pap_smear_done', models.ForeignKey(default=0, on_delete=django.db.models.deletion.PROTECT, related_name='physical_exam_anal_pap_smear_done', to='prep_app.yesnocode')),
                ('anal_pap_smear_result', models.ForeignKey(default=0, on_delete=django.db.models.deletion.PROTECT, related_name='physical_exam_anal_pap_smear_result', to='prep_app.papsmearresultcode')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='prep_app.client')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='%(app_label)s_%(class)s_created_by', related_query_name='%(app_label)s_%(class)ss', to=settings.AUTH_USER_MODEL)),
                ('deleted_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='%(app_label)s_%(class)s_deleted_by', related_query_name='%(app_label)s_%(class)ss', to=settings.AUTH_USER_MODEL)),
                ('family_planning_method', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='physical_exam_family_planning_method', to='prep_app.familyplanningmethodcode')),
                ('hiv_category', models.ForeignKey(default=0, on_delete=django.db.models.deletion.PROTECT, to='prep_app.hivcategorycode')),
                ('mammogram_done', models.ForeignKey(default=0, on_delete=django.db.models.deletion.PROTECT, related_name='physical_exam_mammogram_done', to='prep_app.yesnocode')),
                ('mammogram_result', models.ForeignKey(default=0, on_delete=django.db.models.deletion.PROTECT, to='prep_app.mammogramresultcode')),
                ('modified_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='%(app_label)s_%(class)s_modified_by', related_query_name='%(app_label)s_%(class)ss', to=settings.AUTH_USER_MODEL)),
                ('nontreponemal_result', models.ForeignKey(default=0, on_delete=django.db.models.deletion.PROTECT, related_name='physical_exam_nontreponemal_result', to='prep_app.nontreponemalresultcode')),
                ('pap_smear_done', models.ForeignKey(default=0, on_delete=django.db.models.deletion.PROTECT, related_name='physical_exam_pap_smear_done', to='prep_app.yesnocode')),
                ('pap_smear_result', models.ForeignKey(default=0, on_delete=django.db.models.deletion.PROTECT, related_name='physical_exam_pap_smear_result', to='prep_app.papsmearresultcode')),
                ('patient_stability_status', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='physical_exam_patient_stability_status', to='prep_app.patientstabilitystatuscode')),
                ('pregnant', models.ForeignKey(default=0, on_delete=django.db.models.deletion.PROTECT, related_name='physical_exam_pregnant', to='prep_app.yesnocode')),
                ('psa_done', models.ForeignKey(default=0, on_delete=django.db.models.deletion.PROTECT, related_name='physical_exam_psa_done', to='prep_app.yesnocode')),
                ('psa_result', models.ForeignKey(default=0, on_delete=django.db.models.deletion.PROTECT, related_name='physical_exam_psa_result', to='prep_app.papsmearresultcode')),
                ('respiratory_rate', models.ForeignKey(default=0, on_delete=django.db.models.deletion.PROTECT, to='prep_app.respiratoryratecode')),
                ('smoker', models.ForeignKey(default=0, on_delete=django.db.models.deletion.PROTECT, related_name='physical_exam_smoker', to='prep_app.yesnocode')),
                ('syphilis_done', models.ForeignKey(default=0, on_delete=django.db.models.deletion.PROTECT, related_name='physical_exam_syphilis_done', to='prep_app.yesnocode')),
                ('treponemal_result', models.ForeignKey(default=0, on_delete=django.db.models.deletion.PROTECT, related_name='physical_exam_treponemal_result', to='prep_app.treponemalresultcode')),
                ('urinalysis', models.ForeignKey(default=0, on_delete=django.db.models.deletion.PROTECT, related_name='physical_exam_urinalysis', to='prep_app.urinalysiscode')),
            ],
            options={
                'default_permissions': ('add', 'change', 'delete', 'view', 'list'),
            },
        ),
        migrations.CreateModel(
            name='Parish',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('modified_on', models.DateTimeField(auto_now=True, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('name', models.CharField(max_length=255)),
                ('code', models.CharField(max_length=255)),
                ('abbreviation', models.CharField(default='Unk', max_length=10)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='%(app_label)s_%(class)s_created_by', related_query_name='%(app_label)s_%(class)ss', to=settings.AUTH_USER_MODEL)),
                ('deleted_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='%(app_label)s_%(class)s_deleted_by', related_query_name='%(app_label)s_%(class)ss', to=settings.AUTH_USER_MODEL)),
                ('modified_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='%(app_label)s_%(class)s_modified_by', related_query_name='%(app_label)s_%(class)ss', to=settings.AUTH_USER_MODEL)),
                ('region', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='prep_app.regioncode')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='OtherLab',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('modified_on', models.DateTimeField(auto_now=True, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('test_date', models.DateField()),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='prep_app.client')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='%(app_label)s_%(class)s_created_by', related_query_name='%(app_label)s_%(class)ss', to=settings.AUTH_USER_MODEL)),
                ('deleted_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='%(app_label)s_%(class)s_deleted_by', related_query_name='%(app_label)s_%(class)ss', to=settings.AUTH_USER_MODEL)),
                ('facility', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='prep_app.facility')),
                ('lab_test_name', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='otherlab_lab_test_name', to='prep_app.labtestcode')),
                ('modified_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='%(app_label)s_%(class)s_modified_by', related_query_name='%(app_label)s_%(class)ss', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('modified_on', models.DateTimeField(auto_now=True, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('name', models.CharField(max_length=255)),
                ('code', models.CharField(max_length=255)),
                ('description', models.CharField(blank=True, max_length=255, null=True)),
                ('address', models.CharField(blank=True, max_length=255, null=True)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='%(app_label)s_%(class)s_created_by', related_query_name='%(app_label)s_%(class)ss', to=settings.AUTH_USER_MODEL)),
                ('deleted_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='%(app_label)s_%(class)s_deleted_by', related_query_name='%(app_label)s_%(class)ss', to=settings.AUTH_USER_MODEL)),
                ('modified_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='%(app_label)s_%(class)s_modified_by', related_query_name='%(app_label)s_%(class)ss', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['name'],
                'default_permissions': ('add', 'change', 'delete', 'view', 'list'),
                'unique_together': {('name', 'code', 'deleted_at')},
            },
        ),
        migrations.AddField(
            model_name='facility',
            name='organization',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='facility_organization', to='prep_app.organization'),
        ),
        migrations.AddField(
            model_name='facility',
            name='parish',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='facility_parish', to='prep_app.parish'),
        ),
        migrations.CreateModel(
            name='EmergencyContact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('modified_on', models.DateTimeField(auto_now=True, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('date', models.DateField()),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('age_in_years', models.IntegerField(blank=True, null=True)),
                ('street_name', models.CharField(blank=True, max_length=255, null=True)),
                ('telephone_cell', models.CharField(blank=True, max_length=255, null=True)),
                ('telephone_home', models.CharField(blank=True, max_length=255, null=True)),
                ('telephone_work', models.CharField(blank=True, max_length=255, null=True)),
                ('notes', models.TextField(blank=True, null=True)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='prep_app.client')),
                ('community', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='emergency_contact_community', to='prep_app.communitycode')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='%(app_label)s_%(class)s_created_by', related_query_name='%(app_label)s_%(class)ss', to=settings.AUTH_USER_MODEL)),
                ('deleted_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='%(app_label)s_%(class)s_deleted_by', related_query_name='%(app_label)s_%(class)ss', to=settings.AUTH_USER_MODEL)),
                ('modified_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='%(app_label)s_%(class)s_modified_by', related_query_name='%(app_label)s_%(class)ss', to=settings.AUTH_USER_MODEL)),
                ('parish', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='emergency_contact_parish', to='prep_app.parish')),
                ('relationship_to_patient', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='address_occupation', to='prep_app.relationshipcode')),
            ],
            options={
                'default_permissions': ('add', 'change', 'delete', 'view', 'list'),
            },
        ),
        migrations.AddField(
            model_name='communitycode',
            name='parish',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='prep_app.parish'),
        ),
        migrations.AddField(
            model_name='client',
            name='marital_status',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='prep_app.maritalstatuscode'),
        ),
        migrations.AddField(
            model_name='client',
            name='modified_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='%(app_label)s_%(class)s_modified_by', related_query_name='%(app_label)s_%(class)ss', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='client',
            name='sex_at_birth',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='prep_app.gendercode'),
        ),
        migrations.CreateModel(
            name='ARVMedication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('report_date', models.DateField()),
                ('due_date', models.DateField(blank=True, null=True)),
                ('notes', models.TextField(blank=True, null=True)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='prep_app.client')),
                ('duration', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='prep_app.monthdurationcode')),
                ('regimen', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='prep_app.regimen')),
            ],
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_at_address', models.DateField()),
                ('street_name', models.CharField(blank=True, max_length=255, null=True)),
                ('telephone_cell1', models.CharField(blank=True, max_length=255, null=True)),
                ('telephone_cell2', models.CharField(blank=True, max_length=255, null=True)),
                ('notes', models.TextField(blank=True, null=True)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='prep_app.client')),
                ('community', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='address_community', to='prep_app.communitycode')),
                ('parish', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='prep_app.parish')),
            ],
        ),
        migrations.CreateModel(
            name='UserFacilityAssignment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('modified_on', models.DateTimeField(auto_now=True, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('date', models.DateField(blank=True, null=True)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='%(app_label)s_%(class)s_created_by', related_query_name='%(app_label)s_%(class)ss', to=settings.AUTH_USER_MODEL)),
                ('deleted_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='%(app_label)s_%(class)s_deleted_by', related_query_name='%(app_label)s_%(class)ss', to=settings.AUTH_USER_MODEL)),
                ('facility', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='prep_app.facility')),
                ('modified_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='%(app_label)s_%(class)s_modified_by', related_query_name='%(app_label)s_%(class)ss', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['user__username', 'facility__name'],
                'default_permissions': ('add', 'change', 'delete', 'view', 'list'),
                'unique_together': {('user', 'facility')},
            },
        ),
        migrations.CreateModel(
            name='CD4Count',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('modified_on', models.DateTimeField(auto_now=True, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('test_date', models.DateField()),
                ('test_result', models.IntegerField()),
                ('disa_reference_id', models.CharField(blank=True, max_length=255, null=True)),
                ('notes', models.TextField(blank=True, null=True)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='prep_app.client')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='%(app_label)s_%(class)s_created_by', related_query_name='%(app_label)s_%(class)ss', to=settings.AUTH_USER_MODEL)),
                ('deleted_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='%(app_label)s_%(class)s_deleted_by', related_query_name='%(app_label)s_%(class)ss', to=settings.AUTH_USER_MODEL)),
                ('modified_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='%(app_label)s_%(class)s_modified_by', related_query_name='%(app_label)s_%(class)ss', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'default_permissions': ('add', 'change', 'delete', 'view', 'list'),
                'unique_together': {('test_date', 'client')},
            },
        ),
    ]
