import random

# start_val = input("Plese enter a starting number")
# last_val = input("Please enter a ending number")
# how_many = input("how many guess you can guess this number")

num = random.randint(1,100)
print(num)
tyrs = 6

times = 0

print("Guess a  number between 1 and 100")


while times < 5:
	tyrs = tyrs -1
	print("you have guess left" ,tyrs)

	GuessNum = int(input("Guess a number : "))
	if num == GuessNum:
		print("You guessed it right you guees in times",times)
		break

	elif num < GuessNum:
		print("your guessing higher number try lower")
		times = times  +1

	elif num > GuessNum:
		print("Your guessing lower number try higher")
		times = times  + 1

else:
	print("sorry your five chance or over")