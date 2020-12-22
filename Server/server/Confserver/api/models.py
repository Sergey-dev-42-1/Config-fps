from django.db import models

# Create your models here.
class Motherboard(models.Model):
    Title = models.CharField(max_length=20, null=True)
    Socket = models.CharField(max_length=10,null=True)
    TypeOfSupportedMemory = models.CharField(max_length=10,null=True)
    MaximumSupportedMemoryFrequency =models.IntegerField(null=True)
    AvailabilityOfM2 = models.BooleanField(null=True)

class CPU(models.Model):
    Title = models.CharField(max_length=20,default="")
    Socket = models.CharField(max_length=10)
    TechnologicalProcess = models.IntegerField()
    NumberOfCores = models.IntegerField()
    NumberOfTthreads = models.IntegerField()
    MaximumFrequency = models.IntegerField()
    TypeOfSupportedMemory = models.CharField(max_length=10)
    MaximumFrequencyOfSupportedMemory = models.IntegerField()
    TDP = models.IntegerField()

class GPU(models.Model):
    Title = models.CharField(max_length=20 ,default="")
    TechnologicalProcess = models.IntegerField()
    ChipFfrequency = models.IntegerField()
    TheNumberOfUniversalProcessors = models.IntegerField()
    NumberOfTextureUnits = models.IntegerField()
    TheNumberOfROPUnits = models.IntegerField()
    MemoryType = models.CharField(max_length=10)
    MemoryFrequency = models.IntegerField()
    MemoryCapacity = models.IntegerField()
    TDP = models.IntegerField()
    NumberOfTensorBlocks = models.IntegerField()

class RAM(models.Model):
    Title = models.CharField(max_length=20,default="")
    Type = models.CharField(max_length=10)
    Volume = models.IntegerField()
    Frequency = models.IntegerField()
    Timings = models.IntegerField()

class Storage(models.Model):
    Title = models.CharField(max_length=20,default="")
    Type = models.CharField(max_length=10)
    Volume = models.CharField(max_length=10)
    RecordingSpeed = models.IntegerField()
    ReadingSpeed = models.IntegerField()
