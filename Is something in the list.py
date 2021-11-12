numlist=list()
inp=input("Enter a number?")
while True:
    if inp=='done':break
    value-float(inp)
    numlist.append(value)
average=sum(numlist)/len(numlist)
print("Average",average)