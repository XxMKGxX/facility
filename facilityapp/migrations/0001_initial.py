# Generated by Django 2.2 on 2019-07-05 01:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Facility',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('facility_name', models.CharField(max_length=32)),
                ('address', models.CharField(max_length=256)),
                ('description', models.TextField()),
                ('length', models.IntegerField()),
                ('width', models.IntegerField()),
                ('height', models.IntegerField()),
                ('floor_area', models.IntegerField()),
                ('site_area', models.IntegerField()),
                ('primary_purpose', models.CharField(choices=[('warehouse', 'Warehouse'), ('production facility', 'Production Facility'), ('offices', 'Offices')], max_length=32)),
            ],
        ),
    ]
