import cx_Oracle
import re
con = cx_Oracle.connect('DIV/1234@127.0.0.1/xe')
cur=con.cursor()

def close(cid):
    cur.execute("update customer_detail set end_date=sysdate where cid=(:cust_id)",{'cust_id':cid})
    cur.execute("insert into admin (select * from customer_detail where cid=(:cust_id))",{'cust_id':cid})
    cur.execute("delete from customer_detail where cid=(:cust_id)",{'cust_id':cid})
    cur.execute("delete from status where cid=(:cust_id)",{'cust_id':cid})
    cur.execute("select min_bal from admin where cid=(:cust_id)",{'cust_id':cid})
    temp=cur.fetchall()
    temp=temp[0][0]
    temp=str(temp)
    print("========================================================================")
    print("Your Account is closed And "+temp+" Rs will be Transfer To your Address")
    print("========================================================================")
    con.commit()
    con.close()
