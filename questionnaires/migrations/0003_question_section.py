# Generated by Django 4.2.2 on 2023-06-22 14:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('questionnaires', '0002_remove_question_help_text_af_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='section',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='questionnaires.section'),
        ),
    ]
