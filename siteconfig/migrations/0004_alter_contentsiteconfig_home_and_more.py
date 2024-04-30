# Generated by Django 5.0.4 on 2024-04-30 09:40

import django_ckeditor_5.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('siteconfig', '0003_contentsiteconfig_home_en_contentsiteconfig_home_es_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contentsiteconfig',
            name='home',
            field=django_ckeditor_5.fields.CKEditor5Field(blank=True),
        ),
        migrations.AlterField(
            model_name='contentsiteconfig',
            name='home_en',
            field=django_ckeditor_5.fields.CKEditor5Field(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='contentsiteconfig',
            name='home_es',
            field=django_ckeditor_5.fields.CKEditor5Field(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='contentsiteconfig',
            name='info',
            field=django_ckeditor_5.fields.CKEditor5Field(blank=True),
        ),
        migrations.AlterField(
            model_name='contentsiteconfig',
            name='info_en',
            field=django_ckeditor_5.fields.CKEditor5Field(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='contentsiteconfig',
            name='info_es',
            field=django_ckeditor_5.fields.CKEditor5Field(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='legalsiteconfig',
            name='cookies',
            field=django_ckeditor_5.fields.CKEditor5Field(blank=True),
        ),
        migrations.AlterField(
            model_name='legalsiteconfig',
            name='cookies_en',
            field=django_ckeditor_5.fields.CKEditor5Field(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='legalsiteconfig',
            name='cookies_es',
            field=django_ckeditor_5.fields.CKEditor5Field(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='legalsiteconfig',
            name='privacy',
            field=django_ckeditor_5.fields.CKEditor5Field(blank=True),
        ),
        migrations.AlterField(
            model_name='legalsiteconfig',
            name='privacy_en',
            field=django_ckeditor_5.fields.CKEditor5Field(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='legalsiteconfig',
            name='privacy_es',
            field=django_ckeditor_5.fields.CKEditor5Field(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='legalsiteconfig',
            name='terms_of_use',
            field=django_ckeditor_5.fields.CKEditor5Field(blank=True),
        ),
        migrations.AlterField(
            model_name='legalsiteconfig',
            name='terms_of_use_en',
            field=django_ckeditor_5.fields.CKEditor5Field(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='legalsiteconfig',
            name='terms_of_use_es',
            field=django_ckeditor_5.fields.CKEditor5Field(blank=True, null=True),
        ),
    ]