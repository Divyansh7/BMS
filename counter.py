import cx_Oracle
con = cx_Oracle.connect('DIV/1234@127.0.0.1/xe')
cur=con.cursor()

def block(cid):
    cur.execute("update status set status='LOCKED' where cid=(:cust_id)",{'cust_id':cid})
    con.commit()
