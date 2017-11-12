##print(type(3))
##x = 3
##x = x*x
##print(x)

##s = input("Enter A Number! : ")
##print(s)
##print(type(s))

##y = float(input("Enter a number: ")) #raw_input doesn't work
##print(y)
##print(type(y))

##x = int(input("Enter a number: "))
##if x % 2 == 0:
##    print("Even")
##else:
##    print("Odd")
##    if x % 3 == 1:
##        print("And not divisible by 3")

##x = int(input("Enter x: "))
##y = int(input("Enter y: "))
##z = int(input("Enter z: "))
##
##if x < y:
##    if x < z:
##        print(x,"is least")
##    else:
##        print(z,"is least")
##else:
##    print(y,"is least")
##
##if x < y:
##    if x < z:
##        print(x,"is least")
##    else:
##        print(z,"is least")
##elif y < z:
##    print(y,"is least")
##else:
##    print(z,"is least")
##
##if x < y and x < z:
##    print(x,"is least")
##elif y < z:
##    print(y,"is least")
##else:
##    print(z,"is least")



        

##Find the cube root of a perfect cube
x = int(input("Enter an integer: "))
answer = 0
while answer*answer*answer < abs(x):
    answer = answer + 1
    print("current guess =", answer)

print("Last guess = ",answer)
print("answer*answer*answer =", answer*answer*answer)

if answer*answer*answer == abs(x):
    if x < 0:
        answer = -answer
    print("Cube root of",str(x),"is",str(answer))
else:
    print(x,"is not a perfect cube")



##Checking if we entered negative number or not

##if answer*answer*answer != abs(x):
##    print(x,"is not a perfect cube")
##else:
##    print("You entered a negative number!")
##    answer = -answer
####    if x < 0:
####        answer = answer - 1
##    print("Cube root of",str(x),"is",str(answer))




##userBirthday = input("What is your birthday? ")
##userLastname = input("What is your last name? ")
##print(str(userBirthday), str(userLastname))







##x = 3  #Create variable x and assign value 3 to it
##x = x*x  #Bind x to value 9
##print x
##y = raw_input('enter a number:')
##print type(y)
##print y
##y = float(raw_input('Enter a number: '))
##print type(y)
##print y
##print y*y
##
##x = int(raw_input('Enter an integer: '))
##if x%2 == 0:
##    print 'Even'
##else:
##    print 'Odd'
##    if x%3 != 0:
##        print 'And not divisible by 3'
##
##x = int(raw_input('Enter x: '))
##y = int(raw_input('Enter y: '))
##z = int(raw_input('Enter z: '))
##
##if x < y:
##    if x < z:
##        print 'x is least'
##    else:
##        print 'z is least'
##else:
##    print 'y is least'
##
##if x < y:
##    if x < z:
##        print 'x is least'
##    else:
##        print 'z is least'
##elif y < z:
##    print 'y is least'
##else:
##    print 'z is least'  
##
##if x < y and x < z:
##    print 'x is least'
##elif y < z:
##    print 'y is least'
##else:
##    print 'z is least'
##    
##
###Find the cube root of a perfect cube
##x = int(raw_input('Enter an integer: '))
##ans = 0
##while ans*ans*ans < abs(x):
##    ans = ans + 1
##    #print 'current guess =', ans
##if ans*ans*ans != abs(x):
##    print x, 'is not a perfect cube'
##else:
##    if x < 0:
##        ans = -ans
##    print 'Cube root of ' + str(x) + ' is ' + str(ans)
##
##
##
##
##
