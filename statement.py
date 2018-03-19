import cx_Oracle
import datetime
con = cx_Oracle.connect('DIV/1234@127.0.0.1/xe')
cur=con.cursor()

def state(cid):
    print("Enter Details of START Date :")
    date_entry = input('Enter a date in YYYY-MM-DD format :')
    year, month, day = map(int, date_entry.split('-'))
    start_date = datetime.date(year, month, day)
    print("Enter Details of END Date :")
    date_entry = input('Enter a date in YYYY-MM-DD format :')
    year, month, day = map(int, date_entry.split('-'))
    end_date = datetime.date(year, month, day)
    print("===================================================================")
    print("                       Date                |Credit|Debit|Balance")
    cur.execute("select date_,credit,debit,balance from transaction where date_ >=(:date_from) AND date_ <= (:date_to) AND cid=(:cust_id)",{'date_from':start_date,'date_to':end_date,'cust_id':cid})
    for result in cur:
        print(result)
    print("===================================================================")
    #print(cur.fetchall())
    con.commit()
