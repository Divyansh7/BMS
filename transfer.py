import cx_Oracle
import re
import type_account
con = cx_Oracle.connect('DIV/1234@127.0.0.1/xe')
cur=con.cursor()

def trans(cid):
    acc_cid=int(input("Enter the Another Customer_id :"))
    amount=int(input("Enter the Amount To Transfer :"))
    cur.execute("select min_bal from customer_detail where cid=(:user_id)",{'user_id':cid})
    temp=cur.fetchall()
    temp=temp[0][0]
    new_amount=temp-amount
    cur.execute("select min_bal from customer_detail where cid=(:user_id)",{'user_id':acc_cid})
    temp1=cur.fetchall()
    temp1=temp1[0][0]
    new_amount1=temp1+amount
    check=type_account.type_acc(cid,new_amount)
    if check==True:
        cur.execute("insert into transaction values(:cust_id,sysdate,NULL,:amount,:new_amount)",{'amount':amount,'new_amount':new_amount,'cust_id':cid})
        cur.execute("update Customer_Detail set min_bal=(:amount) where cid=(:cust_id)",{'amount':new_amount,'cust_id':cid})
        cur.execute("insert into transaction values(:cust_id,sysdate,:amount,NULL,:new_amount)",{'amount':amount,'new_amount':new_amount1,'cust_id':acc_cid})
        cur.execute("update Customer_Detail set min_bal=(:amount) where cid=(:cust_id)",{'amount':new_amount1,'cust_id':acc_cid})
        print("Success")
    else:
        print("Maintain Minimum Balance Condition")

    con.commit()
