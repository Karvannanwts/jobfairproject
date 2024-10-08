# Generated by Django 5.0.6 on 2024-09-20 06:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobfairapp', '0008_workexperience'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArrearDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('arrears', models.CharField(choices=[('yes', 'Yes'), ('no', 'No')], default='no', max_length=3)),
                ('arrear_count', models.IntegerField(blank=True, null=True)),
                ('primary_table', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jobfairapp.primarytable')),
            ],
        ),
    ]
