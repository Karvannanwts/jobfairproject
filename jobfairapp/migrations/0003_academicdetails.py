# Generated by Django 5.0.6 on 2024-09-19 09:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobfairapp', '0002_personaldetails_primarytable_delete_admin_user_login_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='AcademicDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('institute_name', models.CharField(max_length=200)),
                ('high_qualification', models.CharField(max_length=100)),
                ('stream', models.CharField(max_length=100)),
                ('passed_out', models.CharField(max_length=4)),
                ('primary_table', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jobfairapp.primarytable')),
            ],
        ),
    ]
