fhand=open('mbox-short.txt')
for line in fhand:
    if the line startswith('From'):
        print(line)