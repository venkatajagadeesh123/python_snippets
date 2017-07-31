# name = "Srini" 
# age = 23




print ("Hello world")

print("My name is " + name + "my age " + str(age))

print("My name is %s and my age %d" % (name,age))


print("My name is {name} and my age {age}".format(age=age,name=name))

# this syntc work only python 3.6 
print(f'My name is {name} my age next year {age+1}')


# writing a function to generate stroy 
# this syntax in python 3.X 
def story(name,age,email='basic@gmail.com'):
	return ("My name is {name} and my age {age} and my email is {email}" .format(age=age,name=name,email=email))


def make_upper_and_give_first_twoval(mystr):
	upcasestr = mystr.upper()
	return upcasestr[:2]

	
# name = "srini"
# age = 23
# email = "hello@gmail.com"

# story(name,age,email)
# print(story(age=23,name='srini',email='hello@gmail.com'))

# full_story= story(age=23,name='srini',email='hello@gmail.com') 

# print(full_story)
print(story(age=23,name='srini'))




person = {'name': 'Jenn', 'age': 23}

# sentence = 'My name is ' + person['name'] + ' and I am ' + str(person['age']) + ' years old.'
# print(sentence)


# sentence = 'My name is {} and I am {} years old.'.format(person['name'], person['age'])
# print(sentence)


# sentence = 'My name is {0} and I am {1} years old.'.format(person['name'], person['age'])
# print(sentence)


# tag = 'h1'
# text = 'This is a headline'

# sentence = '<{0}>{1}</{0}>'.format(tag, text)
# print(sentence)


sentence = 'My name is {0} and I am {1} years old.'.format(person['name'], person['age'])
print(sentence)




# pi = 3.14159265

# sentence = 'Pi is equal to {}'.format(pi)

# print(sentence)


sentence = '1 MB is equal to {} bytes'.format(1000**2)

print(sentence)


import datetime

my_date = datetime.datetime(2016, 9, 24, 12, 30, 45)

# print(my_date)

# March 01, 2016

sentence = '{:%B %d, %Y}'.format(my_date)

print(sentence)

# March 01, 2016 fell on a Tuesday and was the 061 day of the year.

sentence = '{:%B %d, %Y} fell on a {} and was the {} day of the year'.format(my_date)

print(sentence)