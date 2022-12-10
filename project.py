def fxn(stng):

	# get all words
	lst = stng.split()
	oupt = ""
	
	# iterate over words
	for word in lst:
	
		# get first letter of each word
		oupt += word[0]
		
	# uppercase oupt
	oupt = oupt.upper()
	return oupt


# input string
inpt1 = "Computer Science Engineering"

# output acronym
print(fxn(inpt1))

# input string
inpt1 = "geeks for geeks"

# output acronym
print(fxn(inpt1))

# input string
inpt1 = "Uttar pradesh"

# output acronym
print(fxn(inpt1))

inpt1 = "Artificial Intelligence"

print(fxn(inpt1))
# Taking user input 
user_input = input("Enter a phrase: ")

# Getting rid of 'of' word using replace() method & Spiliting the user input into individual words using split() method
phrase = (user_input.replace('of', '')).split()

# Initializing an empty string to append the acronym
a = ""

# for loop to append acronym
for word in phrase:
    a = a + word[0].upper()

print(f'Acronym of {user_input} is {a}')
