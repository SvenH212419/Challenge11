import re


nummer = input("nummer? ")

re_nl = r"\+31"
re_be = r"\+32"
re_mobiel = r"^.{3}6"

if re.match(re_nl, nummer):
    print("NL nummer")
    if re.match(re_mobiel, nummer):
        print("Mobiel")
elif re.match(re_be, nummer):
    print("BE nummer")
    if re.match(re_mobiel, nummer):
        print("mobiel")
else:
    print("Geen NL of BE nummer")