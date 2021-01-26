alist = [[1,'Active', 0],
         [2,'Work Complete', 0],
         [3,'QC Needed', 0],
         [4,'Fix Required', 0],
         [5,'Waiting for Merger', 0],
         [6,'Waiting on Validation', 0]]

newlist = ['(1,50)', '(2,10)', '(4,1)', '(7,1)']
newlist = [x.strip('()').split(',') for x in newlist]
countlist = []

for value in range(1,7):
    for item in newlist:
        if value == int(item[0]):
            alist[value-1][2] = int(item[1])
            break

print(alist)









