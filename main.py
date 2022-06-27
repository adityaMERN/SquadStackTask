#i am keeping in mind that the first statement will always be to create a slot.
def createSystem(temp):
    #contain all the output statements 
    respones=[]
    #to store details related to a particular age
    age={}
    #to store details related to a particular slot
    slotdata={}
    #to store details related to a particular reg no
    regno={}
    firstCommand=temp[0]
    #to check if we dot have any slot or we have an empty line in the input file


    if (firstCommand=='' or firstCommand[0]!='C'  ) and len(respones)==0:
        return "No slots available, can't process the request. create a slot first"
    


    if firstCommand[0]=="C":
        l=firstCommand.split(" ")
        statement="Create a parking lot of "+l[1]+ " slots."
        for i in range(1,int(l[1])+1):
            slotdata[i]=[]
        respones.append(statement)
    #print(slotdata)
    #print(temp)


    for i in range(1,len(temp)):
            command=temp[i]
            firstCmd=temp[0]
            l=firstCmd.split(" ")
            totalslots=l[1]
            #print(command)
            #if the command is to park a vehicle
            if command[0]=="P":
                l=command.split(" ")
                regVal=l[1]
                ageVal=l[3]
                for key in range(1,int(totalslots)+1):
                    if slotdata[key]==[]:
                        slotdata[key]=[ageVal,regVal]
                        break
                statement="Car with vehicle registration number "+ regVal +" has been parked at slot number " +str(key)
                respones.append(statement)
                #the map for storing the slots will look like:
                #{
                #   1:[21,"KA-01-HH-1234"],
                #   2:[22,"KA-01-HH-1235"]
                # }
                if ageVal not in age:
                    age[ageVal]=[[regVal,key]]
                else:
                    age[ageVal].append([regVal,key])
                #the map for storing the age will look like:
                #{
                #    21:[['KA-01-HH-1234',1],['KA-01-HH-12345',2]],
                #    22:[["KA-01-HH-12346",3]]
                #}

                regno[regVal]=[ageVal,key]
                #the map for storing the age will look like:
                #{
                #    KA-01-HH-1234:[21,1]
                #}
                
            #if a vehicle leaves the parking. I am just removing the data of that car
            if command[0]=="L":
                l=command.split(" ")
                slotVal=l[1]
                #print(slotdata)
                for key in range(1,int(totalslots)+1):
                    #print(key)
                    if key==int(slotVal):
                        registrationNo=slotdata[key][1]
                        ageNo=slotdata[key][0]
                        strageNo=str(ageNo)
                        #deleted the entry of that vehicle from slots
                        slotdata[key]=[]
                        ##deleted the entry of that vehicle from agemap
                        for agevalue in age:
                            if agevalue==ageNo:
                                values=age[ageNo]
                                for each in values:
                                    if each[1]==key:
                                        indexval=values.index(each)
                                        values.pop(indexval)
                        #deleted the entry of that vehicle from registrationNO map
                        regno.pop(registrationNo)
                        statement="Slot number "+ str(key)+ " vacated, the car with vehicle registration number " +  registrationNo +  " left the space, the driver of the car was of age "+ str(strageNo)
                        respones.append(statement)

           
            if command[0]=="S":
                l=command.split(" ") 
                 #if slot number is asked for particular age
                if l[0]=="Slot_numbers_for_driver_of_age":
                    ageNo=l[1]
                    slotList=[]
                    for key in age:
                        if key==ageNo:
                            datatobeSearched=age[key]
                            for each in datatobeSearched:
                                slotList.append(each[1])
                    respones.append(','.join(str(x) for x in slotList))


                #if slot number is asked for particluar reg no
                if l[0]=="Slot_number_for_car_with_number":
                    regiNO=l[1]
                    for key in regno:
                        if key==regiNO:
                            slotvalue=regno[regiNO][1]
                    respones.append(slotvalue)

            
            # reg no for particular age
            if command[0]=="V":
                l=command.split(" ")
                ageNo=l[1]
                if ageNo in age:
                    agelist=[]
                    for each in age[ageNo]:
                        agelist.append(each[0])
                    if len(agelist)>0:
                        respones.append(','.join(str(x) for x in agelist))
                    else:
                        respones.append("No cars ")
            # reg no for particular slot  
            

            #if command[0=="S"]
    #print(age)
    #print(slotdata)
    #print(regno)
    return respones

#reading the input from the file named as input.txt
temp = open("input.txt",'r').read().splitlines()

answerValue=createSystem(temp)
#printing the commands on new line in terminal. 
for each in answerValue:
    print(each)
