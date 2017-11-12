
##So the problem is to write a program the prints the
##numbers from 1 to 100, but for multiples of three, print fizz instead of the number.
##And for multiples of 5, print buzz. And if there are multiples are both 3 and 5, print
##fizzbuzz.

for i in range(1,101):
    s = str(i)
    if i % 3 == 0 or i % 5 == 0:
        s = ""
        if i % 3 == 0:
            s = s + "Fizz"
        if i % 5 == 0:
            s = s + "Buzz"
    print(s)
