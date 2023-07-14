# Generated by Django 4.2.2 on 2023-06-27 15:25

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('sites', '0002_alter_domain_unique'),
    ]

    operations = [
        migrations.CreateModel(
            name='LegalSiteConfig',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('terms_of_use', ckeditor.fields.RichTextField(blank=True)),
                ('terms_of_use_en', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('terms_of_use_es', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('privacy', ckeditor.fields.RichTextField(blank=True)),
                ('privacy_en', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('privacy_es', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('cookies', ckeditor.fields.RichTextField(blank=True)),
                ('cookies_en', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('cookies_es', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('site', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='sites.site')),
            ],
        ),
    ]
