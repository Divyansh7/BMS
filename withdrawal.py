import cx_Oracle
import type_account
con = cx_Oracle.connect('DIV/1234@127.0.0.1/xe')
cur=con.cursor()

def withdr(cid):
    cur.execute("SELECT min_bal from Customer_Detail where cid=(:c)",{'c':cid})
    temp=cur.fetchall()
    new_amount=temp[0][0]
    amount=int(input("Withdraw Amount :"))
    new_amount=new_amount-amount
    check=type_account.type_acc(cid,new_amount)
    if check==True:
        cur.execute("insert into transaction values(:cust_id,sysdate,NULL,:amount,:new_amount)",{'amount':amount,'new_amount':new_amount,'cust_id':cid})
        cur.execute("update Customer_Detail set min_bal=(:amount) where cid=(:cust_id)",{'amount':new_amount,'cust_id':cid})
        print("Success")
    else:
        print("======================================")
        print("Maintain Minimum Balance Condition")
        print("======================================")
    con.commit()
