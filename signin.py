import cx_Oracle
import submenu
import re
import display
con = cx_Oracle.connect('DIV/1234@127.0.0.1/xe')
cur=con.cursor()

def cust(cid,password,counter):
    cur.execute("select status from status where cid=(:cust_id)",{'cust_id':cid})
    temp1=cur.fetchall()
    temp1=temp1[0][0]
    if re.match(temp1,'UNLOCKED'):
        cur.execute("SELECT password FROM Customer_Detail where cid=(:cust) or password=(:password)",{'cust':cid,'password':password})
        temp=cur.fetchall()
        temp=temp[0][0]
        if re.search(password,temp):
            print("==========Customer_Details============")
            display.disp_detail(cid)
            print("======================================")
            submenu.sub_menu(cid,password)
            counter=0
            return counter
        else:
            print("==================================")
            print("Invalid User And Password")
            print("==================================")
            counter=counter+1
            return counter
    else:
        print("=========================================")
        print("ID is Blocked, Tell admin to unlock it")
        print("=========================================")
    con.commit()
