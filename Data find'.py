data='From jero@gmail.com.ac.ke Sat Jan 5 09:16 2021'
atpos=data.find('@')
print(atpos)

atpos=data.find('',atpos)
print(atpos)

host=data(atpos+1: sppos)
print(host)