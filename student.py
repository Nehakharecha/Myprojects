#STUDENT DATA

data={}                                 #Create dictionary
print("Enter Your Choice:")
print("1. Press 1 to ADD Data.")
print("2. Press 2 to UPDATE Data.")
print("3. Press 3 to DELETE Data.")
print("4. Press 4 to SEARCH Data.")
print("5. Press 5 to VIEW ALL Data.")

choice="1"
while(choice!="0"):
    choice=input("Enter Your Choice: ")
    if choice=="1":
        roll=input("Enter Roll no: ")
        nm=input("Enter Name: ")
        mb=input("Enter Mob no.: ")
        em=input("Enter Email:")
        ct=input("Enter City:")

        stud_data = dict(rollno=roll,name = nm, mob = mb, email = em,city=ct)
        data[roll] = stud_data                  #Append Data 
        print("Data Added Successfully!!")
    
    elif(choice=="2"):
        num=input("Enter Roll no. To Update Data:")
        
        #search roll no:

        if num in data:                         #Search roll no.
            print("Data found")
            
            nm=input("Enter name: ")
            mb=input("Enter mob: ")
            em=input("Enter email:")
            ct=input("Enter city:")
           
            stud_data = dict(rollno=num, name=nm, mob=mb, email=em, city=ct)
            data[num] = stud_data               #replace/update data
        else:       
            print("No data exists...")

    elif(choice=="3"):
         num=input("Enter Roll no. To Delete Data:")
         
         if num in data:
            data.pop(num)                       #Delete data-->pop()
            print("Data Deleted Successfully!!")
            
         else:
            print("No data exists...")
    elif(choice=="4"):
            num=input("Enter Roll no. To Search Data:")
            
            if num in data:                     #Search Rolll no.
                print(data[num])
               
            else:
                print("No Data Exists...")

    elif(choice=="5"):
        if data=={}:
            print("No Data Exists...")
        else:
            print(data)                         #Print Data
    