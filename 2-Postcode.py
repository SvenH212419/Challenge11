import re


adres = input("type hier je adres: ")
postcode = r"[0-9]{4}? [a-zA-Z]{2}"
output = re.findall(postcode, adres)
for i in output:
    print(i)