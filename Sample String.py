#string in a specific format 
#print("Twinkle, twinkle, little star, \n\tHow I wonder what you are! \n\t\tUp above the world so high, \n\t\tLike a diamond in the sky. \nTwinkle, twinkle, little star, \n\tHow I wonder what you are!")
#print("hello\ngood\n\tif i  am\n\t\thello,hii,\n\t\tgood for any thing\nhello\n\thow are you")

#Version info

'''import sys
print("Python version")
print (sys.version)
print("Version info.")
print (sys.version_info)'''

# display the current date and time.

'''import datetime
now = datetime.datetime.now()
print ("Current date and time : ")
print (now.strftime("%Y-%m-%d %H:%M:%S"))'''

# Area of a Circle

'''from math import pi
r = float(input ("Input the radius of the circle : "))
print ("The area of the circle with radius " + str(r) + " is: " + str(pi * r**2))'''

#first and last name

'''fname = "Manzoorli"
lname = "Shaik"
print ("Hello  " + lname + " " + fname)'''

#Python list:

'''values = "helo world, data"
list = values.split(",")
tuple = tuple(list)
print('List : ',list)
print('Tuple : ',tuple)'''

#Extracting extension from filename in Python

'''filename = "filename.android"
f_extns = filename.split(".")[-1]
print ("The extension of the file is : " + repr(f_extns))'''

# first and last colors from the following list

'''color_list = ["Red","Green","White" ,"Black"]
print( "%s %s"%(color_list[0],color_list[-1]))'''

#lenth of array and position of array
'''horsemen = ["hello", "hii", "good", "special"]

for i in [0, 3, 2, 3]:
    print(horsemen[i])

horsemen = ["hello", "hii", "good", "special"]

for h in horsemen:
    print(h)'''

#print the calendar of a given month and year.

'''import calendar
y = int(input("Input the year : "))
m = int(input("Input the month : "))
print(calendar.month(y, m))'''

# calculate number of days between two dates

'''from datetime import date
f_date = date(2014, 7, 2)
l_date = date(2014, 7, 11)
delta = l_date - f_date
print(delta.days,"Days")'''

# if condition
def difference(n):
    if n <= 17:
        return 17 - n
    else:
        return (n - 17) * 2 

print(difference(22))
print(difference(14))

