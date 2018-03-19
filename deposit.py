import cx_Oracle
con = cx_Oracle.connect('DIV/1234@127.0.0.1/xe')
cur=con.cursor()

def dep(cid):
    cur.execute("SELECT min_bal from Customer_Detail where cid=(:c)",{'c':cid})
    temp=cur.fetchall()
    new_amount=temp[0][0]
    amount=int(input("Deposit Amount :"))
    new_amount=new_amount+amount
    cur.execute("insert into transaction values(:cust,sysdate,:credit,NULL,:new)",{'cust':cid,'credit':amount,'new':new_amount})
    cur.execute("update Customer_Detail set min_bal=(:new) where cid=(:cust)",{'cust':cid,'new':new_amount})
    con.commit()
