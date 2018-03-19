import cx_Oracle
import re
con = cx_Oracle.connect('DIV/1234@127.0.0.1/xe')
cur=con.cursor()

def unblock_cid():
    cur.execute("select count(cid) from status where status='LOCKED'")
    temp=cur.fetchall()
    count=temp[0][0]
    cur.execute("select cid,status from status where status='LOCKED'")
    temp=cur.fetchall()
    for i in range(0,count):
        print(str(temp[i][0])+','+temp[i][1])
    cid=int(input("Enter Customer_ID You Want to Unlock :"))
    cur.execute("select cid,status from status where cid=(:cust_id)",{'cust_id':cid})
    temp=cur.fetchall()
    temp1=temp[0][0]
    temp2=temp[0][1]
    if re.match(temp2,'LOCKED'):
        if(temp==cid):
            cur.execute("update status set status='UNLOCKED' where cid=(:cust_id)",{'cust_id':cid})
            print("UNLOCKED")
        else:
            print("INVALID Customer_ID")
    else:
        print("Already UNLOCKED")
    con.commit()
        

