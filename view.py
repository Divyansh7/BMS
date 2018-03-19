import cx_Oracle
con = cx_Oracle.connect('DIV/1234@127.0.0.1/xe')
cur=con.cursor()

def view_customer():
    cur.execute("select * from customer_detail")
    for result in cur:
        print(result)
    con.commit()
    
