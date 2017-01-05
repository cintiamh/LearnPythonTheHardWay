my_name = 'Zed A. Shaw'
my_age = 35 # not a lie
my_height = 74 # inches
my_weight = 180 # lbs
my_eyes = 'Blue'
my_teeth = 'White'
my_hair = 'Brown'

print "Let's talk about %s." % my_name
print "He's %d inches tall." % my_height
print "He's %d pounds heavy." % my_weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (my_eyes, my_hair)
print "His teeth are usually %s depending on the coffee." % my_teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (
    my_age, my_height, my_weight, my_age + my_height + my_weight)

# How to replace a character in a string with a variable?
my_grade = 'A'
print "My grade was %c." % my_grade

# How to replace a signed integer decimal in a string with a variable?
cups = 6
temperature = -10
print "I have %d cups of water" % cups
print "It's around %i celcius temperature." % temperature

# How to replace a generic value in a string with a variable?
days = 365
print "The year has %r days." % days
bob = "Bob"
print "His name is %r." % bob

# How to replace a string value in a string with a variable? (converted with str())
days = 365
print "The year has %s days." % days
bob = "Bob"
print "His name is %s." % bob
