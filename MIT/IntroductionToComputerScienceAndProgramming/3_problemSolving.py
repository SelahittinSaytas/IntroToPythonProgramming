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

###Find the cube root of a perfect cube
##x = int(raw_input('Enter an integer: '))
##for ans in range(0, abs(x)+1):
##    if ans**3 == abs(x):
##        break
##if ans**3 != abs(x):
##    print x, 'is not a perfect cube'
##else:
##    if x < 0:
##        ans = -ans
##    print 'Cube root of ' + str(x) + ' is ' + str(ans)
##
##x = 25
##epsilon = 0.01
##numGuesses = 0
##ans = 0.0
##while abs(ans**2 - x) >= epsilon and ans <= x:
##    ans += 0.00001
##    numGuesses += 1
##print 'numGuesses =', numGuesses
##if abs(ans**2 - x) >= epsilon:
##    print 'Failed on square root of', x
##else:
##    print ans, 'is close to square root of', x
##
##x = 12345
##epsilon = 0.01
##numGuesses = 0
##low = 0.0
##high = x
##ans = (high + low)/2.0
##while abs(ans**2 - x) >= epsilon and ans <= x:
##    #print low, high, ans
##    numGuesses += 1
##    if ans**2 < x:
##        low = ans
##    else:
##        high = ans
##    ans = (high + low)/2.0
###print 'numGuesses =', numGuesses
##print ans, 'is close to square root of', x

##def withinEpsilon(x, y, epsilon):
##    """x, y, epsilon all ints or floats
##       returns true if x is within epsilon of y"""
##    return abs(x - y) <= epsilon
##
##if withinEpsilon(25, 26, 1):
##    print 'yes'
##else:
##    print 'no'
##
##if withinEpsilon(25, 26, 0.9):
##    print 'yes'
##else:
##    print 'no'










##Find the cube root of a perfect cube

##x = int(input("Enter an integer: "))
##
##for answer in range(0, abs(x)+1):
##    if answer**3 == abs(x):
##        break
##if answer**3 != abs(x):
##    print(x,"is not a perfect cube")
##else:
##    if x < 0:
##        answer = -answer
##    print("Cube root of ",str(x),"is",str(answer))



##Another Example Square root

##x = 12345
##epsilon = 0.01
##numGuesses = 0
##answer = 0
##while abs(answer**2 - x) >= epsilon and answer <= x:
##    answer += 1
##    #answer += 0.00001
##    numGuesses += 1
##print("numGuesses =",numGuesses)
##if abs(answer**2 - x) >= epsilon:
##    print("Failed on square root of",x)
##else:
##    print(answer,"is close to square root of", x)



##
##for name in "John", "Sam", "Jill":
##    print("Hello " + name)
##
##
##
##for i in range(10):
##    print(i)
##
##
##total = 0
##for i in 5, 7, 11, 13:
##    print(i)
##    total = total + i
##
##print(total)



##
##for _ in range(10):
##    print("Hello!")



##for drink in list_of_beverages:
##    print("Would you like a " + drink + "?")



##for i in range(10):
##    turtle.forward(15)
##    turtle.penup()
##    turtle.forward(5)
##    turtle.pendown()
##
##for i in range(10):
##    print(i)



##for _ in range(4):
##    turtle.forward(100)
##    turtle.left(90)

