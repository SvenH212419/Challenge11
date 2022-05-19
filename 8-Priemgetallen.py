import math


def is_priem(n):
    if n < 1:
        return False
    root_n = math.sqrt(n)
    list_upto_root_n = []
    for i in range(int(root_n)+1):
        if i > 1:
            list_upto_root_n.append(i)
    for j in list_upto_root_n:
        if n % j == 0:
            return False
    return True

out = []
for k in range(100):
    if is_priem(k):
        out.append(k)
print(out)