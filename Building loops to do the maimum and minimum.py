numlist=list()
while True:
    inp=input("Enter the number:")
    if inp=='done':break
    value=float(inp)
    numlist.append(value)
average=sum(numlist)/len(numlist)
print ('Average:',average)

