
numberofdays = int(input("numbberof days temperature?:"))
total = 0
samplearray = []
for number in range (numberofdays):
    numberofdayshightemperature = int(input("DAY"+ str(number+ 1)+"high temperature"))
    samplearray.append(numberofdayshightemperature)
    total += samplearray[number]
average = round(total/numberofdays)
    
print ("the average temperature is "+ str(average) + " from the above days")

above = 0

for i in samplearray:
    if i > average:
        above += 1
        
print(str(above)+ " days above averagae ")


    

