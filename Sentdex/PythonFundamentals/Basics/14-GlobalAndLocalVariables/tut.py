
x = 9;

'''
def example():
    print(x)
    print(x+5)
    x+=6
'''

def example():
    global x
    print(x)
    x+=10
    print(x)

def example2():
    globex = x
    print(globex)
    globex+=10
    print(globex)
    return globex

example()

x = example2()
print(x)
