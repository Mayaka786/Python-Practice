name=input("Enter file:")
handle=open(name)
counts=dict()
for line in handle:
    words=line.split()
    for words in words:
    counts[word]=count.get(word,0)+1
    
    bigcount=None
    bigword=None
    for word,coung in counts.items()
    if bigcount
    is None or count> bigcount:
        bigword=word
        bigcount=count
print(bigword, bigcount) 