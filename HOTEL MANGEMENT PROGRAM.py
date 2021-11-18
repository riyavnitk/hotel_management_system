#HOTEL MANAGEMENT SYSTEM
import random as r
from datetime import date
import mysql.connector as sqlc
conn=sqlc.connect(host='localhost',user='riyavardhan',password='riyav')
a=conn.cursor()
try:
    q1="CREATE DATABASE MOTI_MAHAL_HOTELS"
    a.execute(q1)
    conn.commit()
    q2="USE MOTI_MAHAL_HOTELS"
    a.execute(q2)
    conn.commit()
    q3='CREATE TABLE REGISTRATION_DETAILS(DOB DATE,REG_NO INT(6) PRIMARY KEY NOT NULL,FNAME VARCHAR(20),LNAME VARCHAR(20),CITIZENSHIP VARCHAR(30),NATIONAL_IDNO VARCHAR(20),GENDER VARCHAR(1),PHONE_NO VARCHAR(13),ADDRESS VARCHAR(50),EMAIL VARCHAR(30),NO_MEMBERS INT(3))'
    a.execute(q3)
    conn.commit()
    q4="CREATE TABLE ROOM_DETAILS(ROOM_NO INT(3) PRIMARY KEY,POSITION VARCHAR(10) DEFAULT 'VACANT')"
    a.execute(q4)
    Q1='INSERT INTO ROOM_DETAILS(ROOM_NO)VALUES(101)'
    a.execute(Q1)
    Q2='INSERT INTO ROOM_DETAILS(ROOM_NO)VALUES(102)'
    a.execute(Q2)
    Q3='INSERT INTO ROOM_DETAILS(ROOM_NO)VALUES(103)'
    a.execute(Q3)
    Q4='INSERT INTO ROOM_DETAILS(ROOM_NO)VALUES(104)'
    a.execute(Q4)
    Q5='INSERT INTO ROOM_DETAILS(ROOM_NO)VALUES(105)'
    a.execute(Q5)
    Q6='INSERT INTO ROOM_DETAILS(ROOM_NO)VALUES(201)'
    a.execute(Q6)
    Q7='INSERT INTO ROOM_DETAILS(ROOM_NO)VALUES(202)'
    a.execute(Q7)
    Q8='INSERT INTO ROOM_DETAILS(ROOM_NO)VALUES(203)'
    a.execute(Q8)
    Q9='INSERT INTO ROOM_DETAILS(ROOM_NO)VALUES(204)'
    a.execute(Q9)
    Q10='INSERT INTO ROOM_DETAILS(ROOM_NO)VALUES(205)'
    a.execute(Q10)
    Q11='INSERT INTO ROOM_DETAILS(ROOM_NO)VALUES(301)'
    a.execute(Q11)
    Q12='INSERT INTO ROOM_DETAILS(ROOM_NO)VALUES(302)'
    a.execute(Q12)
    Q13='INSERT INTO ROOM_DETAILS(ROOM_NO)VALUES(303)'
    a.execute(Q13)
    Q14='INSERT INTO ROOM_DETAILS(ROOM_NO)VALUES(304)'
    a.execute(Q14)
    Q15='INSERT INTO ROOM_DETAILS(ROOM_NO)VALUES(305)'
    a.execute(Q15)
    Q16='INSERT INTO ROOM_DETAILS(ROOM_NO)VALUES(401)'
    a.execute(Q16)
    Q17='INSERT INTO ROOM_DETAILS(ROOM_NO)VALUES(402)'
    a.execute(Q17)
    Q18='INSERT INTO ROOM_DETAILS(ROOM_NO)VALUES(403)'
    a.execute(Q18)
    Q19='INSERT INTO ROOM_DETAILS(ROOM_NO)VALUES(404)'
    a.execute(Q19)
    Q20='INSERT INTO ROOM_DETAILS(ROOM_NO)VALUES(405)'
    a.execute(Q20)
    Q21='INSERT INTO ROOM_DETAILS(ROOM_NO)VALUES(501)'
    a.execute(Q21)
    Q22='INSERT INTO ROOM_DETAILS(ROOM_NO)VALUES(502)'
    a.execute(Q22)
    Q23='INSERT INTO ROOM_DETAILS(ROOM_NO)VALUES(503)'
    a.execute(Q23)
    Q24='INSERT INTO ROOM_DETAILS(ROOM_NO)VALUES(504)'
    a.execute(Q24)
    Q25='INSERT INTO ROOM_DETAILS(ROOM_NO)VALUES(505)'
    a.execute(Q25)
    conn.commit()
    q8="CREATE TABLE STAFF(STAFF_NO INT(4) PRIMARY KEY,NAME VARCHAR(30),MOBILE_NO VARCHAR(20),GENDER VARCHAR(1),DESIGNATION VARCHAR(20),SALARY INT(8),NATID_NO VARCHAR(20),EMAIL_ID VARCHAR(30),ACC_NO VARCHAR(20))"
    a.execute(q8)
    conn.commit()
    q9="CREATE TABLE BILL(ROOM_NO INT(6) REFERENCES REGISTRATION_DETAILS(ROOM_NO),ACCOMMODATION INT(6) DEFAULT 0,MEALS INT(6) DEFAULT 0,ADDON INT(6) DEFAULT 0,EVEORG INT(6) DEFAULT 0,TAX INT(6) DEFAULT 0,TOTAL INT(8) DEFAULT 0)"
    a.execute(q9)
    conn.commit()
    q91='INSERT INTO BILL(ROOM_NO)VALUES(101)'
    a.execute(q91)
    conn.commit()
    q92='INSERT INTO BILL(ROOM_NO)VALUES(102)'
    a.execute(q92)
    conn.commit()
    q93='INSERT INTO BILL(ROOM_NO)VALUES(103)'
    a.execute(q93)
    conn.commit()
    q94='INSERT INTO BILL(ROOM_NO)VALUES(104)'
    a.execute(q94)
    conn.commit()
    q95='INSERT INTO BILL(ROOM_NO)VALUES(105)'
    a.execute(q95)
    conn.commit()
    q96='INSERT INTO BILL(ROOM_NO)VALUES(201)'
    a.execute(q96)
    conn.commit()
    q97='INSERT INTO BILL(ROOM_NO)VALUES(202)'
    a.execute(q97)
    conn.commit()
    q98='INSERT INTO BILL(ROOM_NO)VALUES(203)'
    a.execute(q98)
    conn.commit()
    q99='INSERT INTO BILL(ROOM_NO)VALUES(204)'
    a.execute(q99)
    conn.commit()
    q100='INSERT INTO BILL(ROOM_NO)VALUES(205)'
    a.execute(q100)
    conn.commit()
    q101='INSERT INTO BILL(ROOM_NO)VALUES(301)'
    a.execute(q101)
    conn.commit()
    q102='INSERT INTO BILL(ROOM_NO)VALUES(302)'
    a.execute(q102)
    conn.commit()
    q103='INSERT INTO BILL(ROOM_NO)VALUES(303)'
    a.execute(q103)
    conn.commit()
    q104='INSERT INTO BILL(ROOM_NO)VALUES(304)'
    a.execute(q104)
    conn.commit()
    q105='INSERT INTO BILL(ROOM_NO)VALUES(305)'
    a.execute(q105)
    conn.commit()
    q106='INSERT INTO BILL(ROOM_NO)VALUES(401)'
    a.execute(q106)
    conn.commit()
    q107='INSERT INTO BILL(ROOM_NO)VALUES(402)'
    a.execute(q107)
    conn.commit()
    q108='INSERT INTO BILL(ROOM_NO)VALUES(403)'
    a.execute(q108)
    conn.commit()
    q109='INSERT INTO BILL(ROOM_NO)VALUES(404)'
    a.execute(q109)
    conn.commit()
    q110='INSERT INTO BILL(ROOM_NO)VALUES(405)'
    a.execute(q110)
    conn.commit()
    q111='INSERT INTO BILL(ROOM_NO)VALUES(501)'
    a.execute(q111)
    conn.commit()
    q112='INSERT INTO BILL(ROOM_NO)VALUES(502)'
    a.execute(q112)
    conn.commit()
    q113='INSERT INTO BILL(ROOM_NO)VALUES(503)'
    a.execute(q113)
    conn.commit()
    q114='INSERT INTO BILL(ROOM_NO)VALUES(504)'
    a.execute(q114)
    conn.commit()
    q115='INSERT INTO BILL(ROOM_NO)VALUES(505)'
    a.execute(q115)
    conn.commit()
except:
    Q='USE MOTI_MAHAL_HOTELS'
    a.execute(Q)
    conn.commit()
conn.close()

#A module storing the registory details
def registration_details():
    conn=sqlc.connect(host='localhost',user='riyavardhan',password='riyav',database='MOTI_MAHAL_HOTELS')
    a=conn.cursor()
    today=date.today()
    d=today.strftime("%B %d, %Y")
    print()
    print("Today",d,'is your date of booking')
    reg_no=r.randint(100000,999999)
    print()
    print('The registration number generated for you by the system is',reg_no)
    print()
    print('Kindly take a note of this registration number as it may be required for completion of other booking procedures later on')
    print()
    fname=input("First name:")
    lname=input("Last name:")
    citz=input("Citizenship:")
    natid_no=input("National ID card number:")
    gender=input("Gender(M/F):")
    ph_no=int(input("Phone number:"))
    address=input("Residential address:")
    email=input("Email ID:")
    nom=int(input("No.of members:"))
    q="INSERT INTO REGISTRATION_DETAILS VALUES('{}',{},'{}','{}','{}','{}','{}','{}','{}','{}',{})".format(today,reg_no,fname,lname,citz,natid_no,gender,ph_no,address,email,nom)
    a.execute(q)
    conn.commit()
    print("Your details have been registered")
    conn.close()

#A module for processing and selecting the ideal room 
def room_selection():
    conn=sqlc.connect(host='localhost',user='riyavardhan',password='riyav',database='MOTI_MAHAL_HOTELS')
    a=conn.cursor()
    print('Have a look through the packages we offer for accommodation and other purposes')
    print('Press any key to continue...')
    input()
    print('(1) Suite rooms (double bed,AC)            : Rs.7000 per day')
    print('(2) Premium rooms (double bed with AC)     : Rs.6000 per day')
    print('(3) Premium rooms (single bed with AC)     : Rs.4000 per day')
    print('(4) Premium rooms (double bed without AC)  : Rs.3000 per day')
    print('(5) Premium rooms (single bed without AC)  : Rs.2000 per day')
    print()
    d=input('Are you sure you want to continue with purchasing our packages(Y/N):')
    print()
    if d[0].lower()=='y':
        global nor
        nor=int(input('Enter the number of rooms you want:'))
        c=0
        tc=0
        for i in range(nor):
            ch=int(input("Enter your choice of room type(1,2,3,4 or 5):"))
            print()
            if ch==1:
                try:
                    tc+=7000
                    room="SELECT*FROM ROOM_DETAILS WHERE POSITION='VACANT' AND ROOM_NO BETWEEN 101 AND 105"
                    a.execute(room)
                    d=a.fetchall()
                    print('Your room number is',d[0][0])
                    room_no=d[0][0]
                    q='UPDATE ROOM_DETAILS SET POSITION="OCCUPIED" WHERE ROOM_NO={}'.format(room_no)
                    a.execute(q)
                    conn.commit()
                except:
                    print('Your desirable room is not vacant. Kindly try for some other room type')
            elif ch==2:
                try:
                    tc+=6000
                    room="SELECT*FROM ROOM_DETAILS WHERE POSITION='VACANT' AND ROOM_NO BETWEEN 201 AND 205"
                    a.execute(room)
                    d=a.fetchall()
                    print('Your room number is',d[0][0])
                    room_no=d[0][0]
                    q='UPDATE ROOM_DETAILS SET POSITION="OCCUPIED" WHERE ROOM_NO={}'.format(room_no)
                    a.execute(q)
                    conn.commit()
                except:
                    print('Your desirable room is not vacant. Kindly try for some other room type')
            elif ch==3:
                try:
                    tc+=4000
                    room="SELECT*FROM ROOM_DETAILS WHERE POSITION='VACANT' AND ROOM_NO BETWEEN 301 AND 305"
                    a.execute(room)
                    d=a.fetchall()
                    print('Your room number is',d[0][0])
                    room_no=d[0][0]
                    q='UPDATE ROOM_DETAILS SET POSITION="OCCUPIED" WHERE ROOM_NO={}'.format(room_no)
                    a.execute(q)
                    conn.commit()
                except:
                    print('Your desirable room is not vacant. Kindly try for some other room type')
            elif ch==4:
                try:
                    tc+=3000
                    room="SELECT*FROM ROOM_DETAILS WHERE POSITION='VACANT' AND ROOM_NO BETWEEN 401 AND 405"
                    a.execute(room)
                    d=a.fetchall()
                    print('Your room number is',d[0][0])
                    room_no=d[0][0]
                    q='UPDATE ROOM_DETAILS SET POSITION="OCCUPIED" WHERE ROOM_NO={}'.format(room_no)
                    a.execute(q)
                    conn.commit()
                except:
                    print('Your desirable room is not vacant. Kindly try for some other room type')
            elif ch==5:
                try:
                    tc+=2000
                    room="SELECT*FROM ROOM_DETAILS WHERE POSITION='VACANT' AND ROOM_NO BETWEEN 501 AND 505"
                    a.execute(room)
                    d=a.fetchall()
                    print('Your room number is',d[0][0])
                    room_no=d[0][0]
                    q='UPDATE ROOM_DETAILS SET POSITION="OCCUPIED" WHERE ROOM_NO={}'.format(room_no)
                    a.execute(q)
                    conn.commit()
                except:
                    print('Your desirable room is not vacant. Kindly try for some other room type')
            else:
                print('OOPS! You chose an invalid choice')
        print()
        print('The specificed details of your choice of room has been made and stored')
        global rooms_cost
        rooms_cost=tc
        Q='UPDATE BILL SET ACCOMMODATION={} WHERE ROOM_NO={}'.format(rooms_cost,room_no)
        a.execute(Q)
        conn.commit()
    else:
        print('''You can also call us on our toll free number 9482843844 to get further customisation of your choice.
Exiting...''')
    conn.close()

#A module for ordering food
def meals():
    conn=sqlc.connect(host='localhost',user='riyavardhan',password='riyav',database='MOTI_MAHAL_HOTELS')
    a=conn.cursor()
    global meals_cost
    room_no=int(input("Room number:"))
    ch=int(input('''The orders will be taken one by one

What would you like:
1.Breakfast
2.Lunch
3.Snacks
4.Dinner

Enter your choice(1,2,3 or 4):'''))
    bc=lc=sc=dc=0
    if ch==1:
        print()
        f=open('BREAKFAST.txt','r')
        S=f.read()
        print(S)
        L=[70,120,60,50,45,55,30,75,80,60]
        i='yes'
        try:
            while i[0].lower()=='y':
                print()
                icode=int(input('Enter the food code of the item you want:'))
                bc+=L[icode-1]
                meals_cost+=L[icode-1]
                i=input('Do you want to have more items(YES/NO):')
            print('The total cost for breakfast is',bc)
        except:
            print('Invalid food code...')
        f.close()
    elif ch==2:
        print()
        f=open('LUNCH.txt','r')
        S=f.read()
        print(S)
        L=[120,125,145,120,120,200,250,150,175,250,175,300,350,750,125]
        i='yes'
        try:
            while i[0].lower()=='y':
                print()
                icode=int(input('Enter the food code of the item you want:'))
                lc+=L[icode-1]
                meals_cost+=L[icode-1]
                i=input('Do you want to have more items(YES/NO):')
            print('The total cost for lunch is',lc)
        except:
            print('Invalid food code...')
        f.close()
    elif ch==3:
        print()
        f=open('SNACKS.txt','r')
        S=f.read()
        print(S)
        L=[40,30,50,20,25,65,35,25,40,50,155,125,110,125,165]
        i='yes'
        try:
            while i[0].lower()=='y':
                print()
                icode=int(input('Enter the food code of the item you want:'))
                sc+=L[icode-1]
                meals_cost+=L[icode-1]
                i=input('Do you want to have more items(YES/NO):')
            print('The total cost for snacks is',sc)
        except:
            print('Invalid food code...')
        f.close()
    elif ch==4:
        print()
        f=open('DINNER.txt','r')
        S=f.read()
        print(S)
        L=[135,75,80,225,150,185,160,175,85,50]
        i='yes'
        try:
            while i[0].lower()=='y':
                print()
                icode=int(input('Enter the food code of the item you want:'))
                dc+=L[icode-1]
                meals_cost+=L[icode-1]
                i=input('Do you want to have more items(YES/NO):')
            print('The total cost for dinner is',dc)
        except:
            print('Invalid food code...')
        f.close()
    else:
        print('Invalid choice')
    q='UPDATE BILL SET MEALS={} WHERE ROOM_NO={}'.format(meals_cost,room_no)
    a.execute(q)
    conn.commit()
    conn.close()

#A module to select additional provisions of the hotel
def addon_services():
    conn=sqlc.connect(host='localhost',user='riyavardhan',password='riyav',database='MOTI_MAHAL_HOTELS')
    a=conn.cursor()
    room_no=int(input('Room number:'))
    global ct
    print('''Following are the services we provide in addition to our normal facilities.

1. Laundry (Rs.1225)
2. Spa (Rs.3000)
3. Room cleaning (Free)
4. Ironing service (Amount depends upon the clothing items)
5. Swimming (Free, Timings(7 AM - 7 PM))
6. Sports (Free)
7. Gym (Rs.500 )
''')
    i='y'
    while i[0].lower()=='y':
        ads=int(input('Choose a service(1,2,3,4,5,6 or 7):'))
        if ads==1:
            ct+=1225
        elif ads==2:
            ct+=3000
        elif ads==3:
            ct+=0
        elif ads==4:
            ct+=1556
        elif ads==5:
            ct+=0
        elif ads==6:
            ct+=0
        elif ads==7:
            ct+=500
        q="INSERT INTO ADDON_SERVICE(ROOM_NO,SERVICE_NO) VALUES({},'{}')".format(room_no,ads)
        print()
        i=input('Do you want to choose more facilities? [Y/N]:')
        print()
    global cost_addon
    cost_addon=ct
    q='UPDATE BILL SET ADDON={} WHERE ROOM_NO={}'.format(cost_addon,room_no)
    a.execute(q)
    conn.commit()
    print('Thank you for choosing our services! We are happy helping you !')
    conn.close()

#A module for event organisers to use hotel halls
def eventorg():
    conn=sqlc.connect(host='localhost',user='riyavardhan',password='riyav',database='MOTI_MAHAL_HOTELS')
    a=conn.cursor()
    room_no=int(input('Room number:'))
    eve=input('Name of the event to be organised:')
    name=input('Organiser name:')
    org=input('Organisation name:')
    idno=input('National ID card number:')
    date=input('Enter the date or organisation in [YYYY-MM-DD] format:')
    reg_no=r.randint(100000,999999)
    global tce
    hall=int(input('''What hall size do you require?

1. Large
2. Medium
3. Small

Your choice(1,2,3):'''))
    print('The hall number',hall,'has been allotted to you')
    global tc
    d=int(input('Number of days you would require the hall:'))
    if hall==1:
        print('Your large-sized hall has been booked')
        c=15000
        tce+=c*d
        print('The cost of the hall booking is',tce)
    elif hall==2:
        print('Your medium-sized hall has been booked')
        c=12000
        tce+=c*d
        print('The cost of the hall booking is',tce)
    elif hall==3:
        print('Your small-sized hall has been booked')
        c=10000
        tce+=c*d
        print('The cost of the hall booking is',tce)
    else:
        print('Oops! You entered an invalid choice')
    q='UPDATE BILL SET EVEORG={} WHERE ROOM_NO={}'.format(tce,room_no)
    a.execute(q)
    conn.commit()
    conn.close()

#A module to exclusively store the deatils of staff members
def staff():
    conn=sqlc.connect(host='localhost',user='riyavardhan',password='riyav',database='MOTI_MAHAL_HOTELS')
    a=conn.cursor()
    sno=r.randint(1000,9999)
    print('Staff number:',sno)
    name=input('Staff name:')
    mno=input('Mobile number:')
    gender=input('Gender(M/F):')
    desg=input('Designation:')
    salary=int(input('Salary of the staff:'))
    natid_no=input('National ID Card number:')
    eid=input('Email ID:')
    accno=input('Account number:')
    qu="INSERT INTO STAFF VALUES({},'{}','{}','{}','{}',{},'{}','{}','{}')".format(sno,name,mno,gender,desg,salary,natid_no,eid,accno)
    a.execute(qu)
    conn.commit()
    print()
    print('Your details have been entered.')
    conn.close()

#A module to generate the final bill
def bill():
    conn=sqlc.connect(host='localhost',user='riyavardhan',password='riyav',database='MOTI_MAHAL_HOTELS')
    a=conn.cursor()
    r_no=int(input('Room number:'))
    print('Processing details...')
    print()
    print()
    Q='UPDATE BILL SET TAX=0.145*(ACCOMMODATION+MEALS+ADDON+EVEORG) WHERE ROOM_NO={}'.format(r_no)
    a.execute(Q)
    conn.commit()
    Q2='UPDATE BILL SET TOTAL=1.145*(ACCOMMODATION+MEALS+ADDON+EVEORG) WHERE ROOM_NO={}'.format(r_no)
    a.execute(Q2)
    conn.commit()
    q='SELECT*FROM BILL WHERE ROOM_NO={}'.format(r_no)
    a.execute(q)
    data=a.fetchall()
    print('\t\t\t MOTI MAHAL HOTELS')
    print('\t\t\t\t BILL')
    print('Room number            :',data[0][0])
    print()
    print('Accommodation          :',data[0][1])
    print('Meals                  :',data[0][2])
    print('Additional service     :',data[0][3])
    print('Event organisation     :',data[0][4])
    print('Tax (GST)              :',data[0][5])
    print('Total                  :',data[0][6])
    print()
    print('Thank you for choosing Moti Mahal for your stay! We hope you visit again!')
    conn.close()


#_main_#
print()
print('\t\t\t\t WELCOME TO THE MOTI MAHAL HOTELS')
print('\t\t\t\t---------------------------------')
while True:
    print('Are you :')
    print('1. A Customer')
    print('2. An administrator')
    print('3. A staff')
    print('4. About')
    print('5. Exit the Moti mahal page')
    ch=int(input("Enter your choice(1,2,3,4 or 5):"))
    if ch==1:
        print()
        print('---------------------------------------------------')
        print('                  CUSTOMER PAGE                    ')
        print('---------------------------------------------------')
        print('Dear Customer! Welcome to the Moti Mahal Hotel!')
        print('Kindly register into our page to buy packages')
        c=input('Do you want to continue with the registration (yes/no):')
        if c[0].lower()=='y':
            registration_details() #Calling of function
            print('\n'*3)
            input('Press any key to continue . . .')
            print()
            room_selection()       #Calling of function
            input('Press any key to continue . . .')
            print()
            print('Your registration and the required type of room has been successfully reserved for you.')
            print('You may now start with exploring and availing the facilities in our hotel')
            print()
            input('Press any key to continue . . .')
            print()
            meals_cost=0
            ct=0
            tce=0
            while True:
                s=int(input('''Which of the following services you would like to avail...
1. Order food
2. Avail additional facilities
3. Organise an event
4. Exit
Your choice(1,2,3 or 4):'''))
                if s==1:
                    print('----------------------------------------------------')
                    print('                  FOOD ORDERS                       ')
                    print('----------------------------------------------------')
                    meals()        #Calling of function
                    print()
                    input('Press any key to continue . . .')
                    print()
                elif s==2:
                    print('----------------------------------------------------')
                    print('              ADDITIONAL FACILITIES                 ')
                    print('----------------------------------------------------')
                    addon_services() #Calling of function
                    print()
                    input('Press any key to continue . . .')
                    print()
                elif s==3:
                    print('----------------------------------------------------')
                    print('              EVENT ORGANISATION                    ')
                    print('----------------------------------------------------')
                    eventorg()       #Calling of function
                    print()
                    input('Press any key to continue . . .')
                    print()
                elif s==4:
                    print('Exiting . . . .')
                    break
                    input('Press any key to continue . . .')
                    print()
                else:
                    print('Invalid choice')
                    input('Press any key to continue . . .')
                    print()
            print()
            print('Thank you for chosing our services! You may now proceed for the billing')
            input('Press any key to continue . . .')
            print()
            print('------------------------------------------------------')
            print('                     BILL                             ')
            print('------------------------------------------------------')
            for i in range(nor):
                print('___________BILL',(i+1),'__________')
                bill()   #Calling of function
            print()
            print('We hope to see you again')
            print('\n'*5)
            input('Press any key to continue . . .')
        else:
            print('Thank you for visiting our page! We hope to provide you services in the future.')
            input('Press any key to continue . . .')
    elif ch==2:
        #Administrator module
        print('--------------------------------------------------')
        print('                ADMINISTRATOR PAGE                ')
        print('--------------------------------------------------')
        print('LOGIN')
        user=input('Admin username:')
        password=input('Admin password:')
        try:
            c=sqlc.connect(host='localhost',user= user,password= password,database='MOTI_MAHAL_HOTELS')
            a=c.cursor()
            while True:
                print('''What operations would you like to perform?

1. Modify customer details as per their requirement
2. Overviewing the customer's bill
3. Overviewing the staff details
4. Modifying the staff details
5. Delete a staff record
6. Delete a customer record
7. Check out a customer
8. Exit
''')
                s=int(input('Your choice(1,2,3,4,5,6 or 7):'))
                if s==1:
                    print()
                    print('\t\t\t CUSTOMER DATA MODIFICATION')
                    print()
                    try:
                        #Updation of registration details
                        reg_no=int(input('Enter the registration number of the customer whose details are to be modified:'))
                        print('Kindly enter the new or modified details of the customer.')
                        fname=input("First name:")
                        q1="UPDATE REGISTRATION_DETAILS SET FNAME='{}' WHERE REG_NO={}".format(fname,reg_no)
                        a.execute(q1)
                        c.commit()
                        lname=input("Last name:")
                        q2="UPDATE REGISTRATION_DETAILS SET LNAME='{}' WHERE REG_NO={}".format(lname,reg_no)
                        a.execute(q2)
                        c.commit()
                        citz=input("Citizenship:")
                        q3="UPDATE REGISTRATION_DETAILS SET CITIZENSHIP='{}' WHERE REG_NO={}".format(citz,reg_no)
                        a.execute(q3)
                        c.commit()
                        natid_no=input("National ID card number:")
                        q4="UPDATE REGISTRATION_DETAILS SET NATIONAL_IDNO='{}' WHERE REG_NO={}".format(natid_no,reg_no)
                        a.execute(q4)
                        c.commit()
                        gender=input("Gender(M/F):")
                        q5="UPDATE REGISTRATION_DETAILS SET GENDER='{}' WHERE REG_NO={}".format(gender,reg_no)
                        a.execute(q5)
                        c.commit()
                        ph_no=int(input("Phone number:"))
                        q6="UPDATE REGISTRATION_DETAILS SET PHONE_NO='{}' WHERE REG_NO={}".format(ph_no,reg_no)
                        a.execute(q6)
                        c.commit()
                        address=input("Residential address:")
                        q7="UPDATE REGISTRATION_DETAILS SET ADDRESS='{}' WHERE REG_NO={}".format(address,reg_no)
                        a.execute(q7)
                        c.commit()
                        email=input("Email ID:")
                        q8="UPDATE REGISTRATION_DETAILS SET EMAIL='{}' WHERE REG_NO={}".format(email,reg_no)
                        a.execute(q8)
                        c.commit()
                        nm=int(input("No.of members:"))
                        q9="UPDATE REGISTRATION_DETAILS SET NO_MEMBERS={} WHERE REG_NO={}".format(nm,reg_no)
                        a.execute(q9)
                        c.commit()
                        print()
                        print('Details have been successfully updated !')
                        input('Press any key to continue . . .')
                        print()
                    except:
                        print('An unexpected connection error occured! Kindly try again!')
                        input('Press any key to continue . . .')
                        print()
                elif s==2:
                    try:
                        print()
                        print('\t\t\t CUSTOMER BILL OVERVIEW')
                        print()
                        room_no=int(input('Enter the room number of the customer whose billing details you want to view:'))
                        print()
                        q='SELECT*FROM BILL WHERE ROOM_NO={}'.format(room_no)
                        a.execute(q)
                        data=a.fetchall()
                        print('Accommodation     :',data[0][1])
                        print('Food              :',data[0][2])
                        print('Additional service:',data[0][3])
                        print('Event organisation:',data[0][4])
                        print()
                        print('GST               :',data[0][5])
                        print('Total             :',data[0][6])
                        print()
                        input('Press any key to continue . . .')
                        print()
                    except:
                        print('An unexpected error occured! Kindly try again!')
                        print()
                        input('Press any key to continue . . .')
                        print()
                elif s==3:
                    try:
                        print()
                        print('\t\t\t OVERVIEWING THE STAFF DETAILS')
                        sno=int(input('Enter the staff number whose details you want to view:'))
                        q='SELECT*FROM STAFF WHERE STAFF_NO={}'.format(sno)
                        a.execute(q)
                        data=a.fetchall()
                        print('Staff number     :',data[0][0])
                        print('Staff name       ;',data[0][1])
                        print('Mobile number    :',data[0][2])
                        print('Gender           :',data[0][3])
                        print('Designation      :',data[0][4])
                        print('Salary           :',data[0][5])
                        print('National ID no.  :',data[0][6])
                        print('Email ID         :',data[0][7])
                        print('Account number   :',data[0][8])
                        print()
                        input('Press any key to continue . . .')
                        print()
                    except:
                        print('An unexpected error occured or the staff number not found! Kindly try again!')
                        print()
                        input('Press any key to continue . . .')
                        print()
                elif s==4:
                    try:
                        print()
                        print('\t\t\t STAFF DATA MODIFICATION')
                        reg_no=int(input('Enter the staff number whose details are to be modified:'))
                        print('Kindly enter the new or modified details of the staff.')
                        name=input("Staff name:")
                        q1="UPDATE STAFF SET NAME='{}' WHERE STAFF_NO={}".format(name,reg_no)
                        a.execute(q1)
                        c.commit()
                        mno=int(input('Mobile number:'))
                        q2="UPDATE STAFF SET MOBILE_NO={} WHERE STAFF_NO={}".format(mno,reg_no)
                        a.execute(q2)
                        c.commit()
                        gender=input("Gender(M/F):")
                        q3="UPDATE STAFF SET GENDER='{}' WHERE STAFF_NO={}".format(gender,reg_no)
                        a.execute(q3)
                        c.commit()
                        desg=input('Designation:')
                        q4="UPDATE STAFF SET DESIGNATION='{}' WHERE STAFF_NO={}".format(desg,reg_no)
                        a.execute(q4)
                        c.commit()
                        sal=int(input("Salary:"))
                        q5="UPDATE STAFF SET SALARY={} WHERE STAFF_NO={}".format(sal,reg_no)
                        a.execute(q5)
                        c.commit()
                        natid_no=input("National ID card number:")
                        q6="UPDATE STAFF SET NATID_NO='{}' WHERE STAFF_NO={}".format(natid_no,reg_no)
                        a.execute(q6)
                        c.commit()
                        email=input("Email ID:")
                        q7="UPDATE STAFF SET EMAIL_ID='{}' WHERE STAFF_NO={}".format(email,reg_no)
                        a.execute(q7)
                        c.commit()
                        acno=input('Account number:')
                        q8="UPDATE STAFF SET ACC_NO='{}' WHERE STAFF_NO={}".format(acno,reg_no)
                        a.execute(q8)
                        c.commit()
                        print()
                        print('Details have been successfully updated !')
                        print()
                        input('Press any key to continue . . .')
                        print()
                    except:
                        print('An unexpected error occured or the record could not be found! Kindly try again!')
                        print()
                        input('Press any key to continue . . .')
                        print()
                elif s==5:
                    try:
                        print()
                        print('\t\t\t STAFF DATA RECORD DELETION')
                        stno=int(input('Enter staff number whose record you want to delete:'))
                        q="DELETE FROM STAFF WHERE STAFF_NO={}".format(stno)
                        a.execute(q)
                        c.commit()
                        print('Record of the staff has been deleted successfully')
                        print()
                        input('Press any key to continue . . .')
                        print()
                    except:
                        print('An unexpected error occured or the record could not be found! Kindly try again!')
                        print()
                        input('Press any key to continue . . .')
                        print()
                elif s==6:
                    try:
                        print()
                        print('\t\t\t CUSTOMER DATA RECORD DELETION')
                        cno=int(input('Enter registration number whose record you want to delete:'))
                        q="DELETE FROM REGISTRATION_DETAILS WHERE REG_NO={}".format(cno)
                        a.execute(q)
                        c.commit()
                        print('Record of the customer has been deleted successfully')
                        print()
                        input('Press any key to continue . . .')
                        print()
                    except:
                        print('An unexpected error occured or the record could not be found! Kindly try again!')
                        print()
                        input('Press any key to continue . . .')
                        print()
                elif s==7:
                    print('\t\t\t\t CUSTOMER CHECKOUT')
                    rno=int(input('Room number:'))
                    q="UPDATE ROOM_DETAILS SET POSITION='VACANT' WHERE ROOM_NO={}".format(rno)
                    a.execute(q)
                    c.commit()
                    print('Customer has been checked out')
                    print()
                    input('Press any key to continue . . .')
                    print()
                elif s==8:
                    print()
                    print('EXITING...')
                    break
                    input('Press any key to continue . . .')
            c.close()
        except:
            print('KINDLY CHECK YOUR USERNAME AND PASSWORD. TRY AGAIN!')
            input('Press any key to continue . . .')
            print()
    elif ch==3:
        print()
        print('--------------------------------------------------')
        print('                   STAFF PAGE                     ')
        print('--------------------------------------------------')
        print('Thank you for showing interest in joining our community')
        print()
        staff()
        print()
        input('Press any key to continue . . .')
        print()
    elif ch==4:
        print()
        print('--------------------------------------------------')
        print('                 THE CREATOR                      ')
        print('--------------------------------------------------')
        print('1. Riya Vardhan')
        print()
        input('Press any key to continue . . .')
        print()
    elif ch==5:
        print('Exiting permanantly from HOME . . .')
        print()
        break
        input('Press any key to continue . . .')
        print()
    else:
        print('An invalid choice!')
        print()
        input('Press any key to continue . . .')
        print()
