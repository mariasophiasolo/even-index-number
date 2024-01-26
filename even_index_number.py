# printing characters from string that are present at an even index number

# ask user to input stringg
endearment = input('Type a greeting: ')
print ("Original greeting: ", endearment)

# initialize a variable where you can store the length of the string
length =  len(endearment)
# repeat the characters in the string at even indices
print ("Printing only even index chars")
for i in range (0, length - 1, 2):
# then print the character at the even index
    print (endearment [i])