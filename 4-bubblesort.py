input = input("Type hier uw lijst: ")
ongesorteerd = list(input)

for n in range(len(ongesorteerd)-1,0,-1):
    for i in range(n):
        if ongesorteerd[i] > ongesorteerd[i+1]:
            ongesorteerd[i], ongesorteerd[i+1] = ongesorteerd[i+1], ongesorteerd[i]

gesorteerd = str()

for karakter in ongesorteerd:
    gesorteerd = gesorteerd + karakter

print(gesorteerd)