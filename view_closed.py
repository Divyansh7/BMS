import cx_Oracle
con = cx_Oracle.connect('DIV/1234@127.0.0.1/xe')
cur=con.cursor()

def view_c():
    cur.execute("select cid,cfirst,clast,address,state,city,pin,contact,min_bal,type_of_account from admin where end_date<=sysdate")
    for result in cur:
        print(result)
    con.commit()
