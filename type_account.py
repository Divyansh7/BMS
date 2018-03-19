import cx_Oracle
import re
con = cx_Oracle.connect('DIV/1234@127.0.0.1/xe')
cur=con.cursor()

def type_acc(cid,amount):
    cur.execute("SELECT type_of_account from Customer_Detail where cid=(:c)",{'c':cid})
    temp=cur.fetchall()
    temp=temp[0][0]
    if re.match(temp,'SAVING'):
        if amount>=0:
            return True
        else:
            return False
    elif re.match(temp,'CURRENT'):
        if amount>=5000:
            return True
        else:
            return False
