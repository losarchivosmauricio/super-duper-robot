epsilon = 0.01
y = 54.0
guess = y/2.0
numGuesses = 0

while abs (guess*guess - y) >= epsilon:
    numGuesses += 1
    guess = guess - (((guess**2) - y)/(2*guess))
print ('numGuesses = ' +str(numGuesses))
print ('Squeare root of ' + str(y) + 'in about ' + str(guess))

# Newton showed tahat if g is an aproxximation to the root, the 
#  g-p(g)/p`(g)  === guess - (((guess**2) - y)/(2*guess))