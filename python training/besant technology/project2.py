import datetime
import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Sandhiya2509@",
    database="covid19_db"
 )

mycursor=mydb.cursor()
x=datetime.datetime.now()
f=open("test1.txt","r")
print(f.read())
def insert_countrydata():
    sql="insert into country_data(country_id,country_name,deaths,population) values (%s,%s,%s,%s)"
    country_id=input("enter the country_id:")
    country_name=input("enter the country_name:")
    deaths=int(input("enter the deaths:"))
    population=int(input("enter the population:"))
    val=(country_id,country_name,deaths,population)
    mycursor.execute(sql,val)
    mydb.commit()
    print("data saved successfully")
def view_countrydata():
    mycursor.execute("select*from country_data")
    result=mycursor.fetchall()
    for i in result:
     print(i)
def insert_doctorsdata():
    sql="insert into doctors_data(name,age,sex,hospital_name) values (%s,%s,%s,%s)"
    name=input("enter the name:")
    age=int(input("enter the age:"))
    sex=input("enter the sex:")
    hospital_name=input("enter the hospital_name:")
    val=(name,age,sex,hospital_name)
    mycursor.execute(sql,val)
    mydb.commit()
    print("data saved successfully")
def view_doctorsdata():
    mycursor.execute("select*from doctors_data")
    result=mycursor.fetchall()
    for i in result:
     print(i)
def insert_hospitaldata():
    sql="insert into hospital_data(hospital_name,location,beds_available) values (%s,%s,%s)"
    hospital_name=input("enter the hospital_name:")
    location=input("enter the location:")
    beds_available=input("enter the beds_available:")

    val=(hospital_name,location,beds_available)
    mycursor.execute(sql,val)
    mydb.commit()
    print("data saved successfully")
def view_hospitaldata():
    mycursor.execute("select*from hospital_data")
    result=mycursor.fetchall()
    for i in result:
     print(i)
def insert_peopledata():
    sql="insert into people_data(name,age,place,hospital_name) values (%s,%s,%s,%s)"
    name=input("enter the name:")
    age=int(input("enter the age:"))
    place=input("enter the place:")
    hospital_name=input("enter the hospital_name:")
    val=(name,age,place,hospital_name)
    mycursor.execute(sql,val)
    mydb.commit()
    print("data saved successfully")
def view_peopledata():
    mycursor.execute("select*from people_data")
    result=mycursor.fetchall()
    for i in result:
     print(i)
def insert_vaccinedata():
    sql="insert into vaccination_data(name,age,sex,place,vaccine_name) values (%s,%s,%s,%s,%s)"
    name=input("enter the name:")
    age=int(input("enter the age:"))
    sex=input("enter the sex:")
    place=input("enter the place:")
    vaccine_name=input("enter the vaccine_name:")
    val=(name,age,sex,place,vaccine_name)
    mycursor.execute(sql,val)
    mydb.commit()
    print("data saved successfully")
def view_vaccinedata():
    mycursor.execute("select*from vaccination_data")
    result=mycursor.fetchall()
    for i in result:
     print(i)
print("1->insert_countrydata")
print("2->insert_doctorsdata")
print("3->insert_hospitalata")
print("4->insert_peopledata")
print("5->insert_vaccinedata")
print("6->view_countrydata")
print("7->view_doctorsdata")
print("8->view_hospitaldata")
print("9->view_peopledata")
print("10->view_vaccinedata")
try:
 user=int(input("enter your number:"))
 if user==1:
    insert_countrydata()
 elif user==2:
    insert_doctorsdata()
 elif user==3:
     insert_hospitaldata()
 elif user==4:
     insert_peopledata()
 elif user==5:
     insert_vaccinedata()
 elif user==6:
    view_countrydata()
 elif user==7:
    view_doctorsdata()
 elif user==8:
     view_hospitaldata()
 elif user==9:
     view_peopledata()
 elif user==10:
     view_vaccinedata()
 else:
     print("please type 1 or 2 or 3 or 4 or 5 or 6 or 7 or 8 or 9 or 10")
except:
    print("please give a number only")

print(x)


