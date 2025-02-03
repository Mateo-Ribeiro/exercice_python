#exercice 1
def unceasar(coded):
    decoded=""
    for i in coded:
        decoded+=chr(ord(i)-3)
    print(decoded)

#exercice 2
def isolation_utf8():
    user_string=input("type something anything: ")
    isolated=[]
    for i in user_string:
        if ord(i)>127:
            isolated.append(hex(ord(i)))
    print(isolated)

from anyascii import *
#exercice 2 bonus
def utf_to_ascii():
    user_string=input("type something, anything: ")
    print(anyascii(user_string))
utf_to_ascii()