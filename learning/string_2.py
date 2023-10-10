names = "Ayush,Rajpal"
print(names[1:11]) # including the first index but not include the last index 
print(len(names))
nameLen = len(names)
print(names[0:nameLen])
print()
# string are immutable that means they cant be changed 
a = "Ayush"
print(a)
print(a.upper())
print(a.lower())
print("Okay so let us see whether we have changed the existing string or not")
print(a) # that shows the string are immutable
# rstrip is used to remove a specifit character whether it occurs onece or more for the last only;

nameX ="!!Hello!_Ayush!!!"
print(nameX.rstrip("!")) # can be usefull to remove spaces from the last
# replace will replace all the occurence the word 
print(nameX.replace("ayush","Chiku")) # this won't work
print(nameX.replace("Ayush","Chiku")) # but this works

#split will slipt from the given character into a list ex-->

print(nameX.split("_"))
# capatlize is used to capatlized the first word && if any othe letter is by mistakenly capitlized then it will make it small
nameX_1 ="aYuSh raJpal"
print(nameX_1.capitalize()) 
# center is used to move the text in center of the terminal
print(nameX_1.center(50)) # not relative to screen size it is fixed to the number of spaces
print(len(nameX_1))

#count is used to count the occurence of the given word to letter or ect in a string
#endswith is used to tell wether the given string ends with the given thing or not --> true/false
print(nameX.endswith("!!!"))

## endswith with different syntax which finds on the given index about the existace of the thing

print(nameX.endswith("lo!",3,8)) ## since "lo!" is ending at the index 8 other wise false
#find is use to find the word --> only gives the first index of the first occurance
# isalnum() --> bolean to check whether the string is alpha numeric or not 
# isalpha() --> to check that does the string onlly contains alpha
# islower() --> to check whether all the letters are in lower case
# isprintable() --> false if the character present in the string is not printable like -> "\n" ;
# isspase() --> check whether the string contains spaces in it or not
# istitle() --> is the string have first letter capital

