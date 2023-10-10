# a = int(input("Enter your age "))
# print("your age is",a)

# if(a>=18):
#     print("You are an adult so you can drive a car for sure!")
# else:
#     print("Sorry dear you drink milk and sleep")

# here we use "elif" wheras we use else if in c++

num = 50

if(num>100):
    print("num>40")
elif(num >35):
    print("num >45")
elif(num>20):
    print("num >50")
else:
    print("num is rest everything")

print("the if-else statment is exicuted")

#good mornig sir program

import time
timestamp =time.strftime('%H') 
print(timestamp)
if(int(timestamp) < 12):
    print("Good Morning Sir, have a good day ahead")
else:
    print("Good Evening Sir!!")

# python also have switch case type thing named as match
"""
syntax as follows: -->

match x:  # x is a variable
    case 0:
        print("something")
    case _:
        print("default case")

--> here break statment is not needed; <--
--> can use a range of value in default by using conditions
ex - case _ if x!=90:
-->and we can use many default statment because of this
"""
