# Generated by Django 5.0.1 on 2024-01-06 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='yfcase',
            name='yfcaseCaseStatus',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='案件狀態'),
        ),
    ]