counts=dict()
print('What is your name:')
line=input('')
words=line.split()
print('Words',words)
print('Counting')
for word in words:
    counts[word]=count.get(word,0)+ 1
print("Counts",counts)