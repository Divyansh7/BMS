import cx_Oracle
con = cx_Oracle.connect('DIV/1234@127.0.0.1/xe')
cur=con.cursor()

def disp(First,Last):
    '''
    cur.execute("select cid,cfirst,clast,type_of_account,min_bal from customer_detail")
    col=cur.fetchall()
    print("cid   |First_Name|Last_Name|Type_Of_Account|Balance")
    for i in range(0,10):
        col1=col[i][0]
        col2=col[i][1]
        col3=col[i][2]
        col4=col[i][3]
        col5=col[i][4]
        print(str(col1)+"  |  "+col2+"    |  "+col3+"  |    "+col4+"    | "+str(col5))
    '''
    cur.execute("select cid from customer_detail where start_date=sysdate AND cfirst=(:first) AND clast=(:last)",{'first':First,'last':Last})
    temp=cur.fetchall()
    temp=temp[0][0]
    print("Your Customer_ID is :"+str(temp))
    con.commit()
