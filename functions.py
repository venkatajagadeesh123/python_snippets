
# def nameoffunc(name,lname):
# 	return name , age 

# # n ,a  = nameoffunc('sri',23)

# x = nameoffunc('sri')

# # print(n)
# # print(a)

# print(x[0])

# *args
# **kwargs 


# def testfun(name,*args):
# 	print(name)
# 	print(args)

# testfun('srini',23,4,5,'hello')

d = {'name':'srini'}

# print(d['name'])
# print(d.get('name1','name not diffenind'))


# funars order = (name,age ,*args,**kwargs , one= '')



# def kwargsfun(*args,**kwargs):
# 	try:
# 		print("hello mr ",kwargs['name'])
# 	except:
# 		print(args)
# 		print(kwargs)
# 		print("Name not diffend")

# val = str(input("plese enter you name "))
# # print(val)
# kwargsfun(name=val)
# # kwargsfun(name='sai',64)# print(val)
# # kwargsfun(name=val)
# # kwargsfun(name='sai',64)

# print(range(1,100))



# print(xrange(1,100))

# for i in xrange(1,100):
# 	print i


# def duble_num(lst):
# 	emty_lst = []
# 	for i in lst:
# 		emty_lst.append(i*i)
# 	return emty_lst

# def duble_num(lst):
# 	for i in lst:
# 		yield i*i


# mylist = [1,2,3,4,5,6]

# val = duble_num(mylist)

# for i in val:
# 	print(i)


# import time

# # print("startin five sen")

# # time.sleep(5)

# # print("five sec or over")


# def sayhi():
# 	time.sleep(5)
# 	print("You took a nap")

# sayhi()


# print(next(val))
# print(next(val))
# print(next(val))


# newfile = open('test.txt' ,'w')

# newfile.write("hello world\n")
# newfile.write("hello world\n")
# newfile.write("end\n")
# newfile.close()


myfile = open('test.txt','r')
print(myfile.read())
myfile.close()



with open('test.txt','r') as f:
	print(f.read())

	

