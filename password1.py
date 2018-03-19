import re

def key(p,x):
    #p = input("Password :")
    #x = True
    while x:
        if (len(p)<6 or len(p)>12):
            break
        elif not re.search("[a-z]",p):
            break
        elif not re.search("[0-9]",p):
            break
        elif not re.search("[A-Z]",p):
            break
        elif not re.search("[$#@]",p):
            break
        elif re.search("\s",p):
            break
        else:
            #print("Valid Password")
            return False
            #x=False
            #break

    if x:
        print("Not a Valid Password")
        return True
