# Generated by Django 3.1.3 on 2020-12-17 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CPU',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Socket', models.CharField(max_length=10)),
                ('TechnologicalProcess', models.CharField(max_length=10)),
                ('NumberOfCores', models.IntegerField()),
                ('NumberOfTthreads', models.IntegerField()),
                ('MaximumFrequency', models.IntegerField()),
                ('TypeOfSupportedMemory', models.CharField(max_length=10)),
                ('MaximumFrequencyOfSupportedMemory', models.IntegerField()),
                ('TDP', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='GPU',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TechnologicalProcess', models.CharField(max_length=10)),
                ('ChipFfrequency', models.CharField(max_length=10)),
                ('TheNumberOfUniversalProcessors', models.IntegerField()),
                ('NumberOfTextureUnits', models.IntegerField()),
                ('TheNumberOfROPUnits', models.IntegerField()),
                ('MemoryType', models.CharField(max_length=10)),
                ('MemoryFrequency', models.IntegerField()),
                ('MemoryCapacity', models.CharField(max_length=10)),
                ('TDP', models.IntegerField()),
                ('NumberOfTensorBlocks', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Motherboard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Socket', models.CharField(max_length=10)),
                ('TypeOfSupportedMemory', models.CharField(max_length=10)),
                ('MaximumSupportedMemoryFrequency', models.IntegerField()),
                ('AvailabilityOfM2', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='RAM',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Type', models.CharField(max_length=10)),
                ('Volume', models.CharField(max_length=10)),
                ('Frequency', models.IntegerField()),
                ('Timings', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Storage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Type', models.CharField(max_length=10)),
                ('Volume', models.CharField(max_length=10)),
                ('RecordingSpeed', models.CharField(max_length=10)),
                ('ReadingSpeed', models.CharField(max_length=10)),
            ],
        ),
    ]
