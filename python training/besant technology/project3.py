import datetime
import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Sandhiya2509@",
    database="world_tourism_db"
    )
mycursor=mydb.cursor()
x=datetime.datetime.now()
f=open("test1.txt","r")
print(f.read())
def insert_americatripdata():
   sql="insert into america_trip_data(packages,flights,price) values (%s,%s,%s)"
   packages=input("enter the packages:")
   flights=input("enter the flights:")
   price=int(input("enter the price:"))
   val=(packages,flights,price)
   mycursor.execute(sql,val)
   mydb.commit()
   print("data saved successfully")
def view_americatripdata():
    mycursor.execute("select*from america_trip_data")
    result=mycursor.fetchall()
    for i in result:
     print(i)
def insert_francepackage():
    sql="insert into france_package(holidays_package,no_days,price,flights) values (%s,%s,%s,%s)"
    holidays_package=input("enter the holiddays_package:")
    no_days=int(input("enter the no_days:"))
    price=int(input("enter the price:"))
    flights=input("enter the flights:")
    val=(holidays_package,no_days,price,flights)
    mycursor.execute(sql,val)
    mydb.commit()
    print("data saved successfully")
def view_francepackage():
    mycursor.execute("select*from france_package")
    result=mycursor.fetchall()
    for i in result:
     print(i)
def insert_maldhivespackage():
    sql="insert into maldhives_package(holidays_package,no_days,price,flights) values (%s,%s,%s,%s)"
    holidays_package=input("enter the holidays_package:")
    no_days=int(input("enter the no_days:"))
    price=int(input("enter the price:"))
    flights=input("enter the flights:")
    val=(holidays_package,no_days,price,flights)
    mycursor.execute(sql,val)
    mydb.commit()
    print("data saved successfully")
def view_maldhivespackage():
    mycursor.execute("select*from maldhives_package")
    result=mycursor.fetchall()
    for i in result:
     print(i)
def insert_bookingdata():
    sql="insert into booking_data(name,age,gender,place,destination,travel_purpose,flight) values (%s,%s,%s,%s,%s,%s,%s)"
    name=input("enter the name:")
    age=int(input("enter the age:"))
    if age>=18:
        print("you can travel")
    else:
        print("your not eligible to travel")
    gender=input("enter the gender:")
    place=input("enter the place:")
    destination=input("enter the destination:")
    travel_purpose=input("enter the travel_purpose:")
    flight=input("enter the flight:")
    val=(name,age,gender,place,destination,travel_purpose,flight)
    mycursor.execute(sql,val)
    mydb.commit()
    print("data saved successfully")
def view_bookingdata():
    mycursor.execute("select*from booking_data")
    result=mycursor.fetchall()
    for i in result:
     print(i)
def insert_tourismdata():
    sql="insert into tourism_data(country_id,country_name,visitors,year) values (%s,%s,%s,%s)"
    country_id=input("enter the country_id:")
    country_name=(input("enter the country_name:"))
    visitors=input("enter the visitors:")
    year=input("enter the year:")
    val=(country_id,country_name,visitors,year)
    mycursor.execute(sql,val)
    mydb.commit()
    print("data saved successfully")
def view_tourismdata():
    mycursor.execute("select*from tourism_data")
    result=mycursor.fetchall()
    for i in result:
     print(i)
print("1->insert_americatripdata")
print("2->insert_francepackage")
print("3->insert_maldhivespackage")
print("4->insert_bookingdata")
print("5->insert_tourismdata")
print("6->view_americatripdata")
print("7->view_francepackage")
print("8->view_maldhivespackage")
print("9->view_bookingdata")
print("10->view_tourismdata")
try:
 user=int(input("enter your number:"))
 if user==1:
    insert_americatripdata()
 elif user==2:
    insert_francepackage()
 elif user==3:
     insert_maldhivespackage()
 elif user==4:
     insert_bookingdata()
 elif user==5:
     insert_tourismdata()
 elif user==6:
    view_americatripdata()
 elif user==7:
    view_francepackage()
 elif user==8:
     view_maldhivespackage()
 elif user==9:
     view_bookingdata()
 elif user==10:
     view_tourismdata()
 else:
     print("please type 1 or 2 or 3 or 4 or 5 or 6 or 7 or 8 or 9 or 10")
except:
    print("please give a number only")
print(x)



