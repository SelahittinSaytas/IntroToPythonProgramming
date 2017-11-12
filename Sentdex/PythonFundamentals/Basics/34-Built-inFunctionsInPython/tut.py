import math

exNum1 = -5
exNum2 = 5

print(abs(exNum1)) #Simple absolute value - mutlak değer
if abs(exNum1) == exNum2:
    print("These are identical")
#help()

## import time
## help(time)

exList = [1,2,3,4,5,6,7,8,9]
print(max(exList))
print(min(exList))

x = 5.77
print(round(x)) ##Rounds up

y = 5.33
print(round(y)) ##Rounds down

print(math.floor(x))
print(math.ceil(x))

print(math.floor(y))
print(math.ceil(y))

intMe = "55"
print(intMe) ##This is a string
print(int(intMe)) ##This is an integer

if intMe != int(intMe):
    print("Values are the same, but the types are different")

print(float(intMe))

strMe = 77
print(str(strMe))
print(int(strMe))

if int(strMe) != str(strMe):
    print("Values are the same, but the types are different")




##
##
##
##
## 
