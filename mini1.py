import random
import cx_Oracle
import signup
import signin
import password1
import re
import email_address
import admin_sign
import counter
import cid_display
counter1=0
x=True
y=True
z=True

while True:
        print("===================================")    
        print("=         1.Sign UP               =")
        print("=         2.Sign IN               =")
        print("=         3.Admin Sign IN         =")
        print("=         4.Quit                  =")
        print("===================================")
        ch=input("Enter your Choice :")

        if(ch=='1'):
            print("=======================================")
            First_Name=input("First Name :")
            Last_Name=input("Last Name :")
            print("=======================================")
            addr=input("Address :")
            state=input("State :")
            city=input("City :")
            pin=int(input("Pincode :"))
            print("=======================================")
            print("PASSWORD RULES:")
            print("1.It should contain a Capital Alphabetic value.")
            print("2.It should contain a Small Alphabetic value.")
            print("3.It should contain a Numeric value.")
            print("4.It should contain a Special Character.")
            print("5.For eg:Divy@1997")
            while x:
                password=input("Password :")
                x=password1.key(password,x)
            while y:
                confirm_pass=input("confirm password :")
                y=password1.key(confirm_pass,y)
                
            if re.match(password,confirm_pass):
                print("Success")
            print("=======================================")    
            print("Type Account:")
            print("1. Saving Account ")
            print("2. Current Account ")
            tp=input("Enter Your choice:")
            if(tp=='1'):
                type_acc='SAVING'
                balance=0
            elif (tp=='2'):
                    type_acc='CURRENT'
                    balance=5000
            else:
                print("Not in option")
            print("=======================================")
            contact=int(input("Contact :"))
            while z:
                email=input("Email Address :")
                z=email_address.email_addr(email,z)
            print("=======================================")
            signup.new_cust(First_Name,Last_Name,addr,state,city,pin,password,type_acc,contact,email,balance)
            print("Success")
            cid_display.disp(First_Name,Last_Name)
        elif(ch=='2'):
            print("=======================================")
            print("=======================================")
            cid=input("Customer_id :")
            password=input("Password :")
            counter1=signin.cust(cid,password,counter1)
            print("=======================================")
            if(counter1==3):
                counter.block(cid)
        elif(ch=='3'):
            print("=======================================")
            user_name=input("Username :")
            password=input("Password :")
            print("=======================================")
            admin_sign.admin(user_name,password)
        elif(ch=='4'):
            break
        else:
            print("=======================================")
            print("Wrong Choice")
            print("=======================================")




