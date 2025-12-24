r = 'yes'
data = []
ques = []
ques1 = int(input("How many questions?"))
for i in range(ques1):
    ques.append(input("Enter Question?"))
while r == 'yes':
    dataB = []
    for i in ques:
        dataB.append(input(f"{i}: "))
    print(dataB)
    data.append(dataB)
    r = input("Continue?")
print(data)
