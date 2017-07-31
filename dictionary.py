
student = {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci']}

for key, value in student.items():
    print(key, value)



# Return a list by sotred values 

citys = {'three':3,'one':1,'two':2}

# method 1 
k = [(k) for k in sorted(citys,key=citys.get)]

# method 2
n = sorted(citys.items() , key= lambda t : t[1])
 
print (k)


mylist = [1,2,3,4,5,1,2,1,3]

# Return a dict with how meny times duplicate values repeted 


d = {}

for i in mylist:
	if i not in d:
		d[i]= 0
	else:
		d[i] += 1
 
d = {}

for i in mylist:
    d[i] = d.get(i,0)+1



# sort this valu by len of elemnt
 
names = ['matdeman','rachel','matthe0','jhonson']
 
 # exp : {6 [matdeman,jhonson] , 5 [rachel.rachel] }
 
d = {}
 
for name in names:
    key = len(name)
    if key not in d:
        d[key] = []
    d[key].append(name)  
 
d = {}
for name in names:
    key = len(name)
    d.setdefault(key,[]).append(name)   
 