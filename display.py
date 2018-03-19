import cx_Oracle
con = cx_Oracle.connect('DIV/1234@127.0.0.1/xe')
cur=con.cursor()

def disp_detail(cid):
    cur.execute("select cid,cfirst,clast,type_of_account,min_bal from customer_detail where cid=(:cust_id)",{'cust_id':cid})
    col=cur.fetchall()
    col1=col[0][0]
    col2=col[0][1]
    col3=col[0][2]
    col4=col[0][3]
    col5=col[0][4]
    print("cid   |First_Name|Last_Name|Type_Of_Account|Balance")
    print(str(col1)+"  |  "+col2+"    |  "+col3+"  |    "+col4+"    | "+str(col5))
    #print(cur.fetchall())
    con.commit()
