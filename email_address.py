import re

def email_addr(email,z):
    #email=input("Email :")
    match = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$',email)

    if match == None:
        print("Bad Syntax")
        return True
    else:
        return False
