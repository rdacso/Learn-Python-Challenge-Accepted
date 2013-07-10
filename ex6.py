# %d puts a whole number into the string. 
x = "There are %d types of people." % 10 
# we just told python that the variable 'binary' means 'binary'
binary = "binary"
# This is where we told python that 'do_not' meant 'don't'
do_not = "don't"
# We created another variable that used the two earlier variables within a string. It's a short cut. Yay!
y = "Those who know %s and those who %s." % (binary, do_not)
# told python to print the variable x as defined on line 2
print x
# told python to print the variable y as defined on line 8
print y
# I believe %r means that you print it exactly as it is. We made a shortcut to include x without putting it in the string.
print "I also said: %r." % x
# It's the same thing as before. We had them add a string (%s)
print "I also said: '%s'." % y
# We defined hilarious as false
hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

print joke_evaluation % hilarious

w = "this is the left side of..."
e = "a string iwth a right side."

print w + e

