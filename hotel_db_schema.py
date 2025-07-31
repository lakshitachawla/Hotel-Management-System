import mysql.connector as m
mydb=m.connect(host='localhost', user = 'root', password='Lak@2408')
myc=mydb.cursor()
#Creating database 
myc.execute('create database if not exists Hotel')
myc.execute('use Hotel')
#Customer Data Table 
myc.execute('create table if not exists custdata(CustID int primary key, CustName varchar(20), Address varchar(80),Room_Type varchar(20),indate date,outdate date)')
myc.execute("insert into custdata values(101,'Tom','3536 Spring Haven Trail','Duluxe','2022-07-03','2022-07-10')")
myc.execute("insert into custdata values(102,'Robert','86 Near Avenue Road','Penthouse','2022-07-04','2022-07-08')")
myc.execute("insert into custdata values(103,'James','659 Davis Street','Family Suite','2022-07-06','2022-07-14')")
myc.execute("insert into custdata values(104,'Francisco','629 Saint Claire Street','Classic','2022-07-15','2022-07-18')")
myc.execute("insert into custdata values(105,'Andrew','1406 Pine Street','Classic','2022-07-18','2022-07-22')")
myc.execute("insert into custdata values(106,'Louis','48 Avenue Road','Family Suite','2022-07-20','2022-07-29')")
myc.execute("insert into custdata values(107,'Emily','37 Park Street','Duluxe','2022-08-01','2022-08-03')")
myc.execute("insert into custdata values(108,'Rose','338 Green Avenue','Penthouse','2022-08-15','2022-08-22')")
print('custdata created')
#Laundary
myc.execute('create table if not exists laundary(clothid int primary key, cloth_of varchar(15),price int)')
myc.execute("insert into laundary values(1,'Men',12)")
myc.execute("insert into laundary values(2,'Women',10)")
myc.execute("insert into laundary values(3,'Children',7)")
print('laundary created')
#Restaurant Menu Table
myc.execute('create table if not exists restaurant(itemno int primary key, itemname varchar(15),price int)')
myc.execute("insert into restaurant values(1,'Tea',60)")
myc.execute("insert into restaurant values(2,'Coffee',120)")
myc.execute("insert into restaurant values(3,'Cold Drink',70)")
myc.execute("insert into restaurant values(4,'Samosa',95)")
myc.execute("insert into restaurant values(5,'Sandwich',120)")
myc.execute("insert into restaurant values(6,'Dhokla',115)")
myc.execute("insert into restaurant values(7,'Kachori',125)")
myc.execute("insert into restaurant values(8,'Hot Chocolate',170)")
myc.execute("insert into restaurant values(9,'Noodles',200)")
myc.execute("insert into restaurant values(10,'Pasta',250)")
print('restaurant created')
#Room Type Table
myc.execute("create table if not exists roomtype(RId int primary key, Room_Type varchar(20),Per_Night_Charges int,Rooms_Available int)")
myc.execute("insert into roomtype values(1,'Classic',6500,10)")
myc.execute("insert into roomtype values(2,'Duluxe',8000,9)")
myc.execute("insert into roomtype values(3,'Family Suite',14000,6)")
myc.execute("insert into roomtype values(4,'Penthouse',18000,8)")
print('roomtype created')
#SPECIAL SERVICE TABLE
myc.execute("create table if not exists splservice(SNo int primary key, Name varchar(20),Price varchar(10))")
myc.execute("insert into splservice values(1,'Swimming','600')")
myc.execute("insert into splservice values(2,'Spa/Massage','1200')")
myc.execute("insert into splservice values(3,'Rent a Car','400')")
myc.execute("insert into splservice values(4,'Parking','100')")
print('special service created')



