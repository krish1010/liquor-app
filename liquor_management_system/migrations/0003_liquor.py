# Generated by Django 3.0.6 on 2020-05-13 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('liquor_management_system', '0002_aadhaarinfo_aadhaar_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Liquor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('liquor_name', models.CharField(max_length=100)),
                ('liquor_quantity', models.FloatField(default=0.0)),
            ],
        ),
    ]
