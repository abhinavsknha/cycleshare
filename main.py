import mysql.connector

#connect sql with python
db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="aksCODING12"
)

#create database and user table
mycursor = db.cursor()
mycursor.execute("CREATE DATABASE if NOT exists pedalpass")
mycursor.execute("use pedalpass")
mycursor.execute("CREATE TABLE if NOT exists user_info (username varchar(255), email_id varchar(255), phone  BIGINT,password varchar(8), regNo varchar(9), hostel varchar(255))") 

#login or sign up
flag=0
choice=int(input("Enter 1 for login and 2 for signup: "))
while(flag==0):
    if choice==1:
        username=input("\nEnter your username: ")
        password=input("Enter your password: ")
        mycursor.execute("SELECT * FROM user_info WHERE username = %s AND password = %s", (username, password))
        result = mycursor.fetchone()
        if result:
            print("Login Successful !!")
            flag=1
        else:
            print("Username and password do not match. Try again :(")

    elif choice==2:
        username=input("\nEnter your username: ")
        emailid=input("Enter your email ID: ")
        phoneNo=int(input("Enter your phone number: "))
        password=input("Enter your password: ")
        regNo=input("Enter your registration number: ")
        hostel=input("Enter your hostel block and room no.")

        query = "INSERT INTO user_info (username, email_id, phone, password, regNo, hostel) VALUES (%s, %s, %s, %s, %s, %s)"
        values = (username, emailid, phoneNo, password, regNo, hostel)
        mycursor.execute(query, values)
        db.commit()
        print("Sign Up Successful !!")
        flag=1

    else:
        print("Invalid Choice")

mycursor.execute("create table if NOT exists cycle_info (cycleNO int, cycleColour varchar(255), cycleType varchar(255))")
usertype=input("Enter 1 for host and 2 for user")
#if usertype==1:


#close the cursor and connection
mycursor.close()
db.close()
