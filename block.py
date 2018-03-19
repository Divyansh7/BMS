import cx_Oracle
con = cx_Oracle.connect('DIV/1234@127.0.0.1/xe')
cur=con.cursor()

def block_cid():
    cur.execute("select cid from status")
