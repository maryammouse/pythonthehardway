# the line below defines x
x = "There are %d types of people." % 10
# this line defines binary
binary = "binary"
# this line defines do_not
do_not = "don't"
# this line defines y using binary and do_not
y = "Those who know %s and those who %s." % (binary, do_not)

# this line prints x
print x
# this line prints y
print y

# this line prints the next sentence with x
print "I said: %r." % x
# this line prints string with y n it
print "I also said: '%s'." % y

# this line defines hilarious as not true
hilarious = False
# this line defines a sentence using hilarious
joke_evaluation = "Isn't that joke so funny?! %r"

# this next line prints joke with hilarious
print joke_evaluation % hilarious

# this prints one string
w = "This is the left side of..."
# this prints the next string
e = "a string with a right side."

# this joins the previous 2 strings together
print w + e
