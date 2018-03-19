import cx_Oracle
con = cx_Oracle.connect('DIV/1234@127.0.0.1/xe')
cur=con.cursor()

def new_cust(first_name,last_name,addr,state,city,pin,password,type_acc,contact,email,balance):
    cur.execute('insert into Customer_Detail values(s1.NEXTVAL,:first,:last,:addr,:state,:city,:pin,:password,:type,:contact,:email,:bal,sysdate,NULL)',{'first':first_name,'last':last_name,'addr':addr,'state':state,'city':city,'pin':pin,'password':password,'type':type_acc,'contact':contact,'email':email,'bal':balance})
    cur.execute("insert into status values(s1.CURRVAL,'UNLOCKED')")
    #cur.execute("select cid from customer_detail where cid=s1.CURRVAL")
    #print(cur.fetchall())
    con.commit()
