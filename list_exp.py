mylist = [1,2,3,4,6,7,3,1]

emty_lst = []

# create new list wihtout duplicates 

# method 1
def generate_list(lst):
	for i in lst:
		if i in emty_lst:
			pass
		else:
			emty_lst.apppend(i)


# method 2
def generate_list1(lst):
	for i in lst:
		if i not in emty_lst:
			emty_lst.apppend(i)



Slicening 

my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#          0, 1, 2, 3, 4, 5, 6, 7, 8, 9
#        -10,-9,-8,-7,-6,-5,-4,-3,-2,-1

# list[start:end:step]

# print my_list[::-1]


sample_url = 'http://google.com'
print sample_url

# Reverse the url
# print sample_url[::-1]

# # Get the top level domain
# print sample_url[-4:]

# # Print the url without the http://
# print sample_url[7:]

# # Print the url without the http:// or the top level domain
print sample_url[7:-4]



# Mutable
list_1 = ['History', 'Math', 'Physics', 'CompSci']
list_2 = list_1

print(list_1)
print(list_2)

# list_1[0] = 'Art'

# print(list_1)
# print(list_2)


# Immutable
# tuple_1 = ('History', 'Math', 'Physics', 'CompSci')
# tuple_2 = tuple_1

# print(tuple_1)
# print(tuple_2)

# tuple_1[0] = 'Art'

# print(tuple_1)
# print(tuple_2)

# Sets
cs_courses = {'History', 'Math', 'Physics', 'CompSci'}

print(cs_courses)


# Empty Lists
empty_list = []
empty_list = list()

# Empty Tuples
empty_tuple = ()
empty_tuple = tuple()

# Empty Sets
empty_set = {} # This isn't right! It's a dict
empty_set = set()


# dict 
mydict = {"one":1,'two':2} 

# Nested ditcs 
mydict = {'numbers' : {"one":1,'two':2} } 
