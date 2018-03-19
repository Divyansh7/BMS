import cx_Oracle
con = cx_Oracle.connect('DIV/1234@127.0.0.1/xe')
cur=con.cursor()

def addr_ch(cid):
    print("Enter New Address Details :")
    addr=input("Enter New Address :")
    state=input("Enter New State :")
    city=input("Enter New City :")
    pin=input("Enter New Pincode")
    cur.execute("update Customer_Detail set address=(:new),state=(:new_st),city=(:new_city),pin=(:new_pin) where cid=(:cust)",{'new':addr,'cust':cid,'new_st':state,'new_city':city,'new_pin':pin})
    print("success")
    con.commit()
