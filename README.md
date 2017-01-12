# Learn Python The HardWay

Learn Python The Had Way from http://learnpythonthehardway.org/book/

## Index

* [Setup](#setup)
* [A Good First Program](#a-good-first-program)
* [Comments and Pound Characters](#comments-and-pound-characters)
* [Numbers and Math](#numbers-and-math)
* [Variables and Names](#variables-and-names)
* [More Variables and Printing](#more-variables-and-printing)
* [Strings and Text](#strings-and-text)
* [More Printing](#more-printing)
* [Printing Printing](#printing-printing)
* [Printing Printing Printing](#printing-printing-printing)
* [What was that?](#what-was-that)
* [Asking Questions](#asking-questions)
* [Prompting People](#prompting-people)
* [Parameters, Unpacking, Variables](#parameters-unpacking-variables)
* [Prompting and passing](#prompting-and-passing)
* [Reading Files](#reading-files)

## Setup

Mac OS X computers already have Python 2, so do not install Python 3 (or any Python).

To start python, type on your terminal:

```
$ python
```

To exit, type:

```
$ quit()
```

[Back to top](#index)

## A Good First Program

Type the following text into a single file named `ex1.py`. Python works best with files ending in `.py`.

```python
print "Hello World!"
print "Hello Again"
print "I like typing this."
print "This is fun."
print 'Yay! Printing.'
print "I'd much rather you 'not'."
print 'I "said" do not touch this.'
```

In terminal run:

```
$ python src/ex1.py
```

[Back to top](#index)

## Comments and Pound Characters

To write a comment, just use the pound sign `#`:

```python
# A comment, this is so you can read your program later.
```

[Back to top](#index)

## Numbers and Math

Used math symbols:

* `+` plus
* `-` minus
* `/` slash
* `*` asterisk
* `%` percent
* `<` less than
* `>` greater than
* `<=` less-than-equal
* `>=` greater-than-equal

[Back to top](#index)

## Variables and Names

To declare variables, you just need to assign values to names with `=`.
In Python we use `_` the underscore character to compose names.

```python
cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven

print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."
```

[Back to top](#index)

## More Variables and Printing

String formatting operations: https://docs.python.org/2.4/lib/typesseq-strings.html

* `%c`	character
* `%s`	string conversion via str() prior to formatting
* `%i`	signed decimal integer
* `%d`	signed decimal integer
* `%u`	unsigned decimal integer
* `%o`	octal integer
* `%x`	hexadecimal integer (lowercase letters)
* `%X`	hexadecimal integer (UPPERcase letters)
* `%e`	exponential notation (with lowercase 'e')
* `%E`	exponential notation (with UPPERcase 'E')
* `%f`	floating point real number
* `%g`	the shorter of %f and %e
* `%G`	the shorter of %f and %E

```python
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
```

[Back to top](#index)

## Strings and Text

Python knows you want something to be a string when you put either `"` (double-quotes)
or `'` (single-quotes) around the text.

Strings may contain the format characters. You simply put the formatted variables
in the string, and then a `%` character, followed by the variable. If you want
multiple formats in your string to print multiple variables you need to put them
inside `()` separated by `,`.

```python
x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not)

print x
print y

print "I said: %r." % x
print "I also said: '%s'." % y

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

print joke_evaluation % hilarious

w = "This is the left side of..."
e = "a string with a right side."

print w + e
```

[Back to top](#index)

## More Printing

```python
print "Mary had a little lamb."
print "Its fleece was white as %s." % 'snow'
print "And everywhere that Mary went."
print "." * 10  # this. will print . 10 times.

end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

# because the , at the end, it will print Cheese Burger. It would print in new line otherwise.
print end1 + end2 + end3 + end4 + end5 + end6,
print end7 + end8 + end9 + end10 + end11 + end12
```

[Back to top](#index)

## Printing Printing

```python
formatter = "%r %r %r %r"

print formatter % (1, 2, 3, 4)
print formatter % ("one", "two", "three", "four")
print formatter % (True, False, False, True)
print formatter % (formatter, formatter, formatter, formatter)
print formatter % (
    "I had this thing.",
    "That you could type up right.",
    "But it didn't sing.",
    "So I said goodnight."
)
```

[Back to top](#index)

## Printing Printing Printing

```python
# Here's some new strange stuff, remember type it exactly.
days = "Mon Tue Wed Thu Fri Sat Sun"
months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"

print "Here are the days: ", days
print "Here are the months: ", months

print """
There's something going on here.
With the three double-quotes.
We'll be able to type as much as we like.
Even 4 lines if we want, or 5, or 6.
"""
```

[Back to top](#index)

## What was that?

The `\` (backslash) character encodes difficult-to-type characters into a string.

`\\`	Backslash (\)
`\'`	Single-quote (')
`\"`	Double-quote (")
`\a`	ASCII bell (BEL)
`\b`	ASCII backspace (BS)
`\f`	ASCII formfeed (FF)
`\n`	ASCII linefeed (LF)
`\N{name}`	Character named name in the Unicode database (Unicode only)
`\r`	Carriage Return (CR)
`\t`	Horizontal Tab (TAB)
`\uxxxx`	Character with 16-bit hex value xxxx (u'' string only)
`\Uxxxxxxxx`	Character with 32-bit hex value xxxxxxxx (u'' string only)
`\v`	ASCII vertical tab (VT)
`\ooo`	Character with octal value ooo
`\xhh`	Character with hex value hh

```python
tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat
```

Note: If you use `\U` or `\u` then you'll need to use a unicode string in `u'\U0001F47E'`. Put a `u` in front of the `''` (single-quotes) or `""` (double-quotes).

[Back to top](#index)

## Asking Questions

```python
print "How old are you?",
age = raw_input()
print "How tall are you?",
height = raw_input()
print "How much do you weigh?",
weight = raw_input()

print "So, you're %r old, %r tall and %r heavy." % (
    age, height, weight)
```

[Back to top](#index)

## Prompting People

For `raw_input` you can also put in a prompt to show to a person so he knows what to type.
Put a string that you want for the prompt inside the `()`:

```python
y = raw_input("Name? ")
```

```python
age = raw_input("How old are you? ")
height = raw_input("How tall are you? ")
weight = raw_input("How much do you weigh? ")

print "So, you're %r old, %r tall and %r heavy." % (
    age, height, weight)
```

You can check the documentation by typing `pydoc raw_input` in your terminal.

[Back to top](#index)

## Parameters, Unpacking, Variables

We can also write scripts that accepts arguments.

```python
from sys import argv

script, first, second, third = argv

print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third
```

and run like:

```
$ python ex13.py first 2nd 3rd
```

The first line imports argv (argument variable) from sys. The variable holds the
arguments you pass to your Python script when you run it.

The second line unpacks `argv` into separated variables.

The `import` imports what is called `modules`.

[Back to top](#index)

## Prompting and passing

More examples.

```python
from sys import argv

script, user_name = argv
prompt = '> '

print "Hi %s, I'm the %s script." % (user_name, script)
print "I'd like to ask you a few questions."
print "Do you like me %s?" % user_name
likes = raw_input(prompt)

print "Where do you live %s?" % user_name
lives = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)

print """
Alright, so you said %r about liking me.
You live in %r.  Not sure where that is.
And you have a %r computer.  Nice.
""" % (likes, lives, computer)
```

[Back to top](#index)

## Reading Files

We'll have two files: a script file `ex15.py` and a text file: `ex15_sample.txt`.

```
This is stuff I typed into a file.
It is really cool stuff.
Lots and lots of fun to have in here.
```

We want to use the script to open the text file.

```python
from sys import argv

script, filename = argv

txt = open(filename)

print "Here's your file %r:" % filename
print txt.read()

print "Type the filename again:"
file_again = raw_input("> ")

txt_again = open(file_again)

print txt_again.read()
```

The open() command is the method that actually opens the file and returns a
"file object". And the read() method returns the string from the file.

You should use the txt.close() after you are finished with the file.

[Back to top](#index)
