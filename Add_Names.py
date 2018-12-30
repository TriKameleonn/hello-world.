#Input
first_name = input("What is your first name?")
last_name = input("What is your last name?")

#List for values of letters
first_values = []
last_values = []

#Inserting values of letters in first name into list
for letter in first_name:
	if letter.isupper():
		first_values.append(ord(letter) - 64)
	else:
		first_values.append(ord(letter) - 96)

#Inserting values of letters in last name into list
for letter in last_name:
	if letter.isupper():
		last_values.append(ord(letter) - 64)
	else:
		last_values.append(ord(letter) - 96)

#Outputs of sums
print("Sum of first name: ", sum(first_values))
print("Sum of last name: ", sum(last_values))
print("Sum of full name: ", sum(first_values) + sum(last_values))

#Output of averages

#Output of average of first name
first_avg = int(sum(first_values)/len(first_values))
print("Average of first name: ", first_avg)
#print("Corresponding letter: ", )

#Output of average of last name
last_avg = int(sum(last_values)/len(last_values))
print("Average of last name: ", last_avg)

#Output of average of full name
full_avg = int((sum(first_values) + sum(last_values))/(len(first_values)+len(last_values)))
print("Average of full name: ", full_avg)

