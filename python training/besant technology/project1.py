import datetime



import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Sandhiya2509@",
    database="happycollege_db"
 )

mycursor=mydb.cursor()
x=datetime.datetime.now()
f=open("test1.txt","r")
print(f.read())

def insert_studentdata():
    sql= "insert into student_data(admno,rollno,department,name,age,place) values (%s,%s,%s,%s,%s,%s)"
    admno=int(input("enter your admno:"))
    rollno=int(input("enter your rollno:"))
    department=input("enter your department:")
    name=input("enter your name:")
    age=int(input("enter your age:"))
    place=input("enter your place:")
    val=(admno,rollno,department,name,age,place)
    mycursor.execute(sql,val)
    mydb.commit()
    print("data saved successfully")
def view_studentdata():
    mycursor.execute("select*from student_data")
    result=mycursor.fetchall()
    for i in result:
     print(i)
def insert_teacherdata():
    sql="insert into teacher_data(name,age,qualification,department,place) values (%s,%s,%s,%s,%s)"
    name=input("enter your name:")
    age=int(input("enter your age:"))
    qualification=input("enter your qualification:")
    department=input("enter your department:")
    place=input("enter your place:")
    val=(name,age,qualification,department,place)
    mycursor.execute(sql,val)
    mydb.commit()
    print("data saved successfully")
def view_teacherdata():
    mycursor.execute("select*from teacher_data")
    result=mycursor.fetchall()
    for i in result:
     print(i)
def insert_staffdata():
   x=datetime.datetime.now()
   f=open("test1.txt","r")
   print(f.read())
   sql="insert into staff_data(name,age,qualification,occupation,place) values (%s,%s,%s,%s,%s)"
   name=input("enter your name:")
   age=int(input("enter your age:"))
   qualification=input("enter your qualification:")
   occupation=input("enter your occupation:")
   place=input("enter your place:")
   val=(name,age,qualification,occupation,place)
   mycursor.execute(sql,val)
   mydb.commit()
   print("data saved successfully")
def view_staffdata():
    mycursor.execute("select*from staff_data")
    result=mycursor.fetchall()
    for i in result:
     print(i)
def insert_arreardata():
    sql="insert into arrear_data(admno,rollno,department,name,age,arrears,paper) values (%s,%s,%s,%s,%s,%s,%s)"
    admno=int(input("enter your admno:"))
    rollno=int(input("enter your rollno:"))
    department=input("enter your department:")
    name=input("enter your name:")
    age=int(input("enter your age:"))
    arrears=int(input("enter your arrears:"))
    paper=input("enter your paper:")
    val=(admno,rollno,department,name,age,arrears,paper)
    mycursor.execute(sql,val)
    mydb.commit()
    print("data saved successfully")
def view_arreardata():
    mycursor.execute("select*from arrear_data")
    result=mycursor.fetchall()
    for i in result:
     print(i)
def insert_aluminadata():
    sql= "insert into alumina_data(admno,rollno,department,name,age,place) values (%s,%s,%s,%s,%s,%s)"
    admno=int(input("enter your admno:"))
    rollno=int(input("enter your rollno:"))
    department=input("enter your department:")
    name=input("enter your name:")
    age=int(input("enter your age:"))
    place=input("enter your place:")
    val=(admno,rollno,department,name,age,place)
    mycursor.execute(sql,val)
    mydb.commit()
    print("data saved successfully")
def view_aluminadata():
    mycursor.execute("select*from alumina_data")
    result=mycursor.fetchall()
    for i in result:
     print(i)
print("1->insert_studentdata")
print("2->insert_teacherdata")
print("3->insert_staffdata")
print("4->insert_arreardata")
print("5->insert_aluminadata")
print("6->view_studentdata")
print("7->view_teacherdata")
print("8->view_staffdata")
print("9->view_arreardata")
print("10->view_aluminadata")
try:
 user=int(input("enter your number:"))
 if user==1:
    insert_studentdata()
    print("studentdata")
 elif user==2:
    insert_teacherdata()
 elif user==3:
    insert_staffdata()
 elif user==4:
    insert_arreardata()
 elif user==5:
    insert_aluminadata()
 elif user==6:
    view_studentdata()
 elif user==7:
    view_teacherdata()
 elif user==8:
    view_staffdata()
 elif user==9:
    view_arreardata()
 elif user==10:
    view_aluminadata()
 else:
     print("please type 1 or 2 or 3 or 4 or 5 or 6 or 7 or 8 or 9 or 10")
     
     

except:
    print("please give a number only")
print(x)

    
 
    
     
     

