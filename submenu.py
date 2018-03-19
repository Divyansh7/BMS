import cx_Oracle
import addresschange
import deposit
import withdrawal
import statement
import transfer
import closure

def sub_menu(cid,password):
    while True:
         print("=========================================")
         print("=                  MENU                 =")
         print("=            1.Address Change           =")
         print("=            2.Money Deposit            =")
         print("=            3.Money Withdrawal         =")
         print("=            4.Print Statement          =")
         print("=            5.Transfer Money           =")
         print("=            6.Account Closure          =")
         print("=            7.Customer logout          =")
         print("=========================================")
         ch=input("Enter Your Choice :")

         if(ch=='1'):
             addresschange.addr_ch(cid)
         elif (ch=='2'):
            deposit.dep(cid)
         elif (ch=='3'):
            withdrawal.withdr(cid)
         elif (ch=='4'):
            statement.state(cid)
         elif (ch=='5'):
            transfer.trans(cid)
         elif (ch=='6'):
            closure.close(cid)
         else:
            print("======================================")
            print("Successfull Logout")
            print("======================================")
            break
