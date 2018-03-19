import cx_Oracle
import re
import view
import view_closed
import unblock
#import block
con = cx_Oracle.connect('DIV/1234@127.0.0.1/xe')
cur=con.cursor()

def admin(name,password):
    cur.execute("select username from admin_login where password=(:password)",{'password':password})
    temp=cur.fetchall()
    temp=temp[0][0]
    if re.match(name,temp):
        print("================================================")
        print("Logged In")
        print("================================================")
        print("================================================")
        print("=                  MENU                        =")
        print("=         1.View Customer Detail               =")
        print("=      2.View closed account history           =")
        print("=          3.Unlock Customer_ID                =")
        print("=                4.Log Out                     =")
        print("================================================")
        ch=input("Enter Your Choice :")

        if(ch=='1'):
            view.view_customer()
        elif (ch=='2'):
            view_closed.view_c()
        elif (ch=='3'):
            unblock.unblock_cid()
        elif (ch=='4'):
            print("================================================")
            print("Successfull Log Out")
            print("================================================")
    else:
        print("================================================")
        print("Invalid User OR Password, Try Again")
        print("================================================")
