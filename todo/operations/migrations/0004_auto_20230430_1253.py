# Generated by Django 3.0.4 on 2023-04-30 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operations', '0003_auto_20230430_1241'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.CharField(blank=True, choices=[('P', 'Pending'), ('C', 'Completed')], default='P', max_length=10, null=True),
        ),
    ]
