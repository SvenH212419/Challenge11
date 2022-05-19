import re


mail = input("Type hier uw email: ")
patroonemail = r"[a-zA-Z0-9+]+@[a-zA-Z]+.[a-zA-Z]{2,}"
if re.fullmatch(patroonemail, mail): 
    print("Dit is een correcte email")
else:
    print("Deze email is incorrect")