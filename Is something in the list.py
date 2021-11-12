numlist=list()
while True:
    inp=input("What is your number:")
    if inp=='done': break
    value=float(inp)
    numlist.append(value)
average=sum(numlist)/len(numlist)
print("average: ",average)
