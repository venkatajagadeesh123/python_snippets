# myfile = open('test.txt' , 'r')
# print (myfile.read())
# myfile.close()



# with open('test.txt' , 'r') as f :
# 	with open('newfile.txt' , 'w') as n:
# 		for lines in f:
# 			n.write(lines)

# 	with open('newfile.txt','r') as n:
# 		print(n.read())
# try:
# 	with open('test.txt','r') as f:
# 		print (f.read())
# except:
# 	print("file doesn't found")

# with open('test.txt', 'r') as f:
# 	emtylist = []
# 	newlist = []
# 	for words in f:
# 		emtylist.append(words)
# 	for w in emtylist:
# 		if w not in newlist:
# 			newlist.append(w)
# 	with open('test_without_dup.txt' , 'w') as n:
# 		for i in newlist:
# 			n.write(i)


# with open('test.txt', 'r') as f:
# 	emtylist = []
# 	newset = set()
# 	for words in f:
# 		emtylist.append(words)
# 	for w in emtylist:
# 		newset.add(w)
# 		print(newset)
# 	with open('test_without_dup.txt' , 'w') as n:
# 		for i in newset:
# 			n.write(i)
import os 
import csv

# print(os.ci)
with open('stock.csv' , 'r') as f:
	headers = next(f)
	tmpdata = csv.reader(f)
	for rows in tmpdata:
		rows.strip()
		rows.replace(',' , '_')
		rows[1] = (int(float(rows[1])))
		print (rows)

