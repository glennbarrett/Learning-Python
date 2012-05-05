# imports argv from the sys module
from sys import argv

# unpacks argv into script and filename variables (Left to right)
script, filename = argv

# declares a variable 'txt' and sets it as file from argv variable 'filename'
txt = open(filename)

# prints text on screen
print "Here's your file %r:" % filename

# displays text from file stored in variable 'txt'
print txt.read()

# prints "Type the filename again:"
print "Type the filename again:"

# declares variable 'file_again' that will take input from a prompt shown as '> '
file_again = raw_input("> ")

# declares variable 'txt_again' and sets it as file from prompt entry
txt_again = open(file_again)

# displays text from file store in 'txt_again'
print txt_again.read()

txt.close()
txt_again.close()