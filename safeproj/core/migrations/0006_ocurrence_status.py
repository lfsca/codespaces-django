# Generated by Django 5.2.3 on 2025-07-03 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_solution_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='ocurrence',
            name='status',
            field=models.CharField(choices=[('pending', 'Pending'), ('accepted', 'Accepted'), ('rejected', 'Rejected')], default='pending', max_length=10),
        ),
    ]
