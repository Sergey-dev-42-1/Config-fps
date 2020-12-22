from django.shortcuts import render
from django.http import HttpResponse
from django.http.response import JsonResponse
from api import models

# Create your views here.
def create(request):

    models.Motherboard.objects.all().delete()
    models.CPU.objects.all().delete()
    models.GPU.objects.all().delete()
    models.Storage.objects.all().delete()
    models.RAM.objects.all().delete()

    list = []

    #Мать
    list.append(models.Motherboard.objects.create(Title="MSI B460M-A PRO",
                                                  Socket="LGA 1200",
                                                  TypeOfSupportedMemory="DDR4",
                                                  MaximumSupportedMemoryFrequency=2933,
                                                  AvailabilityOfM2=True))

    list.append(models.Motherboard.objects.create(Title="MSI MAG B460 TORPEDO",
                                                  Socket="LGA 1200",
                                                  TypeOfSupportedMemory="DDR4",
                                                  MaximumSupportedMemoryFrequency=2933,
                                                  AvailabilityOfM2=True))

    list.append(models.Motherboard.objects.create(Title="ASRock B460M Steel Legend",
                                                  Socket="LGA 1200",
                                                  TypeOfSupportedMemory="DDR4",
                                                  MaximumSupportedMemoryFrequency=2933,
                                                  AvailabilityOfM2=True))

    #Процы
    list.append(models.CPU.objects.create(Title="Intel i5 10400",
                                          Socket="LGA_1200",
                                          TechnologicalProcess=14,
                                          NumberOfCores=6,
                                          NumberOfTthreads=12,
                                          MaximumFrequency=4300,
                                          TypeOfSupportedMemory="DDR4",
                                          MaximumFrequencyOfSupportedMemory=2666,
                                          TDP=65))

    list.append(models.CPU.objects.create(Title="Intel i5 10600k",
                                          Socket="LGA_1200",
                                          TechnologicalProcess=14,
                                          NumberOfCores=6,
                                          NumberOfTthreads=12,
                                          MaximumFrequency=4800,
                                          TypeOfSupportedMemory="DDR4",
                                          MaximumFrequencyOfSupportedMemory=2666,
                                          TDP=125))

    list.append(models.CPU.objects.create(Title="Intel i5 10100",
                                          Socket="LGA_1200",
                                          TechnologicalProcess=14,
                                          NumberOfCores=4,
                                          NumberOfTthreads=8,
                                          MaximumFrequency=4300,
                                          TypeOfSupportedMemory="DDR4",
                                          MaximumFrequencyOfSupportedMemory=2666,
                                          TDP=65))

    #Видяхи
    list.append(models.GPU.objects.create(Title="PALIT NVIDIA GeForce RTX 3080",
                                          TechnologicalProcess=8,
                                          ChipFfrequency=1860,
                                          TheNumberOfUniversalProcessors=8704,
                                          NumberOfTextureUnits=272,
                                          TheNumberOfROPUnits=88,
                                          MemoryType="GDDR6X",
                                          MemoryFrequency=19000,
                                          MemoryCapacity=10,
                                          TDP=320,
                                          NumberOfTensorBlocks=272))

    list.append(models.GPU.objects.create(Title="Gigabyte GeForce RTX 3060 Ti GAMING OC 8G",
                                          TechnologicalProcess=8,
                                          ChipFfrequency=1740,
                                          TheNumberOfUniversalProcessors=4864,
                                          NumberOfTextureUnits=152,
                                          TheNumberOfROPUnits=80,
                                          MemoryType="GDDR6",
                                          MemoryFrequency=14000,
                                          MemoryCapacity=8,
                                          TDP=200,
                                          NumberOfTensorBlocks=152))

    list.append(models.GPU.objects.create(Title="MSI nVidia GeForce RTX 3070",
                                          TechnologicalProcess=8,
                                          ChipFfrequency=1695,
                                          TheNumberOfUniversalProcessors=5888,
                                          NumberOfTextureUnits=184,
                                          TheNumberOfROPUnits=96,
                                          MemoryType="GDDR6",
                                          MemoryFrequency=14000,
                                          MemoryCapacity=8,
                                          TDP=220,
                                          NumberOfTensorBlocks=184))

    #Оператива
    list.append(models.RAM.objects.create(Title="Neo Forza ENCKE",
                                          Type="DDR4",
                                          Volume=16,
                                          Frequency=3200,
                                          Timings=16))

    list.append(models.RAM.objects.create(Title="Patriot Viper 4 Steel",
                                          Type="DDR4",
                                          Volume=16,
                                          Frequency=3000,
                                          Timings=16))

    list.append(models.RAM.objects.create(Title="HyperX FURY Black",
                                          Type="DDR4",
                                          Volume=16,
                                          Frequency=3200,
                                          Timings=16))

    #Диски
    list.append(models.Storage.objects.create(Title="Toshiba P300",
                                              Type="HDD",
                                              Volume=1000,
                                              RecordingSpeed=196,
                                              ReadingSpeed=196))

    list.append(models.Storage.objects.create(Title="480 GB SSD M.2 storage WD Green",
                                              Type="M.2",
                                              Volume=480,
                                              RecordingSpeed=545,
                                              ReadingSpeed=545))

    list.append(models.Storage.objects.create(Title="Samsung 860 EVO",
                                              Type="SSD",
                                              Volume=500,
                                              RecordingSpeed=520,
                                              ReadingSpeed=550))


    for a in list:
        a.save()

    all_count = models.Motherboard.objects.count()
    all_count+=models.CPU.objects.count()
    all_count += models.GPU.objects.count()
    all_count += models.RAM.objects.count()
    all_count += models.Storage.objects.count()

    all_list_title="Материнские платы:<br>"
    for o in models.Motherboard.objects.all():
        all_list_title+=o.Title+"<br>"

    all_list_title += "Видеокарты:<br>"
    for o in models.GPU.objects.all():
        all_list_title+=o.Title+"<br>"

    all_list_title += "Процессоры:<br>"
    for o in models.CPU.objects.all():
        all_list_title+=o.Title+"<br>"

    all_list_title += "Оперативная память:<br>"
    for o in models.RAM.objects.all():
        all_list_title+=o.Title+"<br>"

    all_list_title += "Диск:<br>"
    for o in models.Storage.objects.all():
        all_list_title+=o.Title+"<br>"

    return HttpResponse("База данных отформатирована и создана снова.<br> Общее число элементов: "+str(all_count)+
                        "<br><br>"+"Список всех элементов:<br>"+all_list_title)

def request(request):
    all_count = models.Motherboard.objects.count()
    all_count += models.CPU.objects.count()
    all_count += models.GPU.objects.count()
    all_count += models.RAM.objects.count()
    all_count += models.Storage.objects.count()

    id = 0
    data = {}

    id_category=0
    for o in models.Motherboard.objects.all():
        now ={}
        now.update({"Id":id})
        now.update({"Title": o.Title})
        now.update({"Socket": o.Socket})
        now.update({"TypeOfSupportedMemory": o.TypeOfSupportedMemory})
        now.update({"MaximumSupportedMemoryFrequency": o.MaximumSupportedMemoryFrequency})
        now.update({"AvailabilityOfM2": o.AvailabilityOfM2})
        data.update({"MB"+str(id_category):now})
        id+=1
        id_category+=1

    id_category = 0
    for o in models.CPU.objects.all():
        now = {}
        now.update({"Id": id})

        now.update({"Title": o.Title})
        now.update({"Socket": o.Socket})
        now.update({"TechnologicalProcess": o.TechnologicalProcess})
        now.update({"NumberOfCores": o.NumberOfCores})
        now.update({"NumberOfTthreads": o.NumberOfTthreads})
        now.update({"MaximumFrequency": o.MaximumFrequency})
        now.update({"TypeOfSupportedMemory": o.TypeOfSupportedMemory})
        now.update({"MaximumFrequencyOfSupportedMemory": o.MaximumFrequencyOfSupportedMemory})
        now.update({"TDP": o.TDP})

        data.update({"CPU" + str(id_category): now})
        id +=1
        id_category+=1

    id_category = 0
    for o in models.GPU.objects.all():
        now = {}
        now.update({"Id": id})

        now.update({"Title": o.Title})
        now.update({"TechnologicalProcess": o.TechnologicalProcess})
        now.update({"ChipFfrequency": o.ChipFfrequency})
        now.update({"TheNumberOfUniversalProcessors": o.TheNumberOfUniversalProcessors})
        now.update({"NumberOfTextureUnits": o.NumberOfTextureUnits})
        now.update({"TheNumberOfROPUnits": o.TheNumberOfROPUnits})
        now.update({"MemoryType": o.MemoryType})
        now.update({"MemoryFrequency": o.MemoryFrequency})
        now.update({"MemoryCapacity": o.MemoryCapacity})
        now.update({"TDP": o.TDP})
        now.update({"NumberOfTensorBlocks": o.NumberOfTensorBlocks})


        data.update({"GPU" + str(id_category): now})
        id +=1
        id_category +=1

    id_category = 0
    for o in models.RAM.objects.all():
        now = {}
        now.update({"Id": id})

        now.update({"Title": o.Title})
        now.update({"Type": o.Type})
        now.update({"Volume": o.Volume})
        now.update({"Frequency": o.Frequency})
        now.update({"Timings": o.Timings})


        data.update({"RAM" + str(id_category): now})
        id +=1
        id_category +=1

    for o in models.Storage.objects.all():
        now = {}
        now.update({"Id": id})

        now.update({"Title": o.Title})
        now.update({"Type": o.Type})
        now.update({"Volume": o.Volume})
        now.update({"RecordingSpeed": o.RecordingSpeed})
        now.update({"ReadingSpeed": o.ReadingSpeed})


        data.update({"Storage" + str(id_category): now})
        id +=1
        id_category +=1



    return JsonResponse(data)