import csv



#open file
f = open('monthwise_data.csv')
#save file in a variable
csv_f = csv.reader(f)
count = -1
for row in csv_f:
    count = count + 1
    #skip row 1
    if(count>0):
        for i in row:
            print(i)


