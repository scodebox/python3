l = []
row = int(input('Enter total number of ROW : '))
column = int(input('Enter total number of COLUMN : '))

for i in range(row):
    temp = []
    for j in range(column):
        temp.append(int(input('Enter value : ')))
    l.append(temp)

print ('Display : \n')
for i in l:
    print (i)