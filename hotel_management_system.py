import mysql.connector 
import getpass

mydb = mysql.connector.connect(host='localhost',user='root', password='Lak@2408',database='hotel')
mycursor=mydb.cursor()

#Welcome Screen
def Menuset():
    print("-"*156)
    print(" Welcome to Deluna Oriental".center(156,'='))
    print("-"*156)
    print("")
    print('Enter 1: For Admin')
    print('Enter 2: For Customer')
    print('Enter 3: To Exit')
    au=int(input('Enter you choice: '))
    if au==1:
        AdminSet()
    elif au==2:
        CustSet()
    elif au==3:
        print('Thanks for using our services')
    else:
        print('Kindly choose from above options')

#For Admin 
def AdminSet():
    print('='*156)
    print(" Welcome Admin ".center(156,'='))
    print("="*156)
    print("")
    ps=getpass.getpass("Enter your password: ")
    if ps=="Hotel_24":
        print("Enter 1: To View Customer Data")
        print("Enter 2: To Register Customer")
        print("Enter 3: To Calculate Room Bill")
        print("Enter 4: To View Room Types Available")
        print("Enter 5: To View Special Services")
        print("Enter 6: To Update Special Services")
        print("Enter 7: To Add Special Service")
        print("Enter 8: To Exit")
        ca=int(input('Enter your choice: '))
        if ca==1:
            viewcust()
        elif ca==2:
            registercust()
        elif ca==3:
            roomrent()
        elif ca==4:
            roomtypeview()
        elif ca==5:
            splservice()
        elif ca==6:
            upsplservices()
        elif ca==7:
            addservice()
        elif ca==8:
            print('Thanks for using our services')
        else:
            print("Kindly choose from above options")
    else:
        print('Inavlid Password')

#For Customers 
def CustSet():
    print('='*156)
    print(" Welcome to Deluna Oriental ".center(156,'='))
    print(" Hope you like our services ".center(156,'='))
    print('='*156)
    print("")
    print('Enter 1: To View Room Types Available')
    print('Enter 2: To Order Food And Beverages')
    print('Enter 3: For Laundary Services')
    print('Enter 4: To View Special Servies')
    print('Enter 5: To Exit')
    uc=int(input('Enter your choice: '))
    if uc==1:
        roomtypeview()
    elif uc==2:
        orderitem()
    elif uc==3:
        laundary()
    elif uc==4:
        splservice()
    elif uc==5:
        print('Thanks for using our services')
    else:
        print('Kindly choose from above options')
    
#To Run Again
def runagain():
    runagn=input("Do you want to run again y/n:")
    if runagn=='y':
        Menuset()
    else:
        print('Thanks for using our services')

#To View Customer Data
def viewcust():
    print(' CUSTOMER DATA '.center(156,'^'))
    mycursor.execute('select * from custdata')
    for rec in mycursor:
        print('Customer ID:',rec[0],'Customer Name:',rec[1],'Address:',rec[2],'Room Type:',rec[3])
        
#To Regitser a Customer 
def registercust():
    print(' REGISTRATION OF A CUSTOMER '.center(156,'^'))
    cid=int(input('Enter the Customer ID: '))
    name=input("Enter Customer Name: ")
    addr=input("Enter Customer's Address: ")
    roomtype=input("Enter Room Type Taken: ")
    indate=input("Enter Check In Date in YYYY/MM/DD :")
    outdate=input("Enter Check Out Date in YYYY/MM/DD :")
    sql="insert into custdata(CustID,CustName,Address,Room_Type,indate,outdate)values({},'{}','{}','{}','{}','{}')".format(cid,name,addr,roomtype,indate,outdate)
    mycursor.execute(sql)
    print('The Customer is successfully registered!')
    mydb.commit()

#To Preview the room types with details available
def roomtypeview():
    print(' ROOM TYPES AVAILABLE '.center(156,'^'))
    mycursor.execute('select * from roomtype')
    for rec in mycursor:
        print('Room ID:',rec[0],'Room Type:',rec[1],'Per Night Charges:',rec[2],'Rooms Available:',rec[3])

#To rent a room to the customer 
def roomrent():
    print(' ROOM RENT '.center(156,'^'))
    mycursor.execute('select * from roomtype')
    for rec in mycursor:
        print('Room ID:',rec[0],'Room Type:',rec[1],'Per Night Charges:',rec[2])
    x=int(input("Enter the Room Id of the Room Customer Stayed in: "))
    n=int(input("For How Many Nights Did Customer Stay: "))
    if(x==1):
        q=1200*n
        print('Your Room Rent is: ',q)
    elif (x==2):
        q=2500*n
        print('Your Room Rent is: ',q)
    elif (x==3):
        q=4000*n
        print('Your Room Rent is: ',q)
    elif (x==4):
        q=6000*n
        print('Your Room Rent is: ',q)
    else:
        print('Kindly choose from the above options')


#To Order from Restaurant 
def orderitem():
    global s
    print(' FOOD AND BEVERAGES '.center(156,'^'))
    sql="select * from restaurant"
    mycursor.execute(sql)
    rows=mycursor.fetchall()
    for x in rows:
            print('Item Number:',x[0],'Item Name:',x[1],'Price:',x[2])
    no=int(input('Enter the Number of items to be ordered: '))
    s=0 #Amount to be paid for the items ordered 
    for i in range (no):
        d=int(input("Enter your choice: "))
        if(d==1):
            a=int(input("Enter quantity: "))
            print("You have ordered",a,'Tea')
            s+=60*a
        elif (d==2):
            a=int(input("Enter quantity: "))
            print("You have ordered",a,"Coffee")
            s+=120*a
        elif(d==3):
            a=int(input("Enter quantity: "))
            print("You have ordered",a,"Cold drink")
            s+=70*a
        elif(d==4):
            a=int(input("Enter quantity: "))
            print("You have ordered",a,"Samosa")
            s+=95*a
        elif(d==5):
            a=int(input("Enter quantity: "))
            print("You have ordered",a,"Sandwich")
            s+=120*a
        elif(d==6):
            a=int(input("Enter quantity: "))
            print("You have ordered",a,"Dhokla")
            s+=115*a
        elif(d==7):
            a=int(input("Enter quantity: "))
            print("You have ordered",a,"Kachori")
            s+=125*a
        elif(d==8):
            a=int(input("Enter quantity: "))
            print("You have ordered",a,"Milk Bottle")
            s+=170*a
        elif(d==9):
            a=int(input("Enter quantity: "))
            print("You have ordered",a,"plate Noodles")
            s+=200*a
        elif(d==10):
            a=int(input("Enter quantity: "))
            print("You have ordered",a,"plate Pasta")
            s+=250*a
        else:
            print("Please enter your choice from the menu")
    print('Total Amount = ',s)
    
    
#For laundary 
def laundary():
    print(' LAUNDARY '.center(156,'^'))
    global z
    z=0
    sql='select* from laundary'
    mycursor.execute(sql)
    for w in mycursor:
        print('S No.:',w[0],'Cloth of:',w[1],'Price Per Cloth:',w[2])
    ym=int(input('Cloths of Men: '))
    yw=int(input('Cloths of Women: '))
    yc=int(input('Cloths of Children: '))
    if ym!=0:
        z+=12*ym
    if yw!=0:
        z+=10*yw
    if yc!=0:
        z+=7*yc
        
    print("Your laundary bill is:",z)

#For Special Services
def splservice():
    print(' SPECIAL SERVICES AVAILABLE '.center(156,'^'))
    mycursor.execute('select * from splservice')
    for rec in mycursor:
        print('Service Name:',rec[1],'Price:',rec[2])
    print('To enjoy these services contact the reception')

#Updating Special Services
def upsplservices():
    print(' TO UPDATE SPECIAL SERVICES '.center(156,'^'))
    mycursor.execute('select * from splservice')
    for rec in mycursor:
        print('SNo.:',rec[0],'Service Name:',rec[1],'Price:',rec[2])
    uc=int(input('Enter the SNo of the Special Service to be updated: '))
    uf=input('Enter the coloumn name to be updated: ')
    uv=input('Enter the new value: ')
    sql1="UPDATE splservice SET {}={} WHERE sno={}".format(uf,uv,uc)
    mycursor.execute(sql1)
    mydb.commit()
    print('Data Updated in the Server')

#Adding a Special Service
def addservice():
    print(' TO ADD A SPECIAL SERVICES '.center(156,'^'))
    mycursor.execute('select * from splservice')
    for rec in mycursor:
        print('SNo.:',rec[0],'Service Name:',rec[1],'Price:',rec[2])
    sno=int(input('Enter SNo of Service: '))
    ns=input("Enter Service Name: ")
    prs=input("Enter Service Price: ")
    sqls="insert into splservice(SNo,Name,Price)values({},'{}','{}')".format(sno,ns,prs)
    mycursor.execute(sqls)
    print('The Service is successfully registered!')
    mydb.commit()
    
    
Menuset()
runagain()


