import sys

##THIS IS USED TO COMMUNICATE BETWEEN OTHER PROGRAMMING LANGUAGES
##SUCH AS BETWEEN PHP AND PYTHON

##sys.stderr.write("This is 'stderr' text!\n")
##sys.stderr.flush()
##sys.stdout.write("This is 'stdout' text!\n")
##
##print(sys.argv) 

##if len(sys.argv) > 1:
##    print(float(sys.argv[1])+5)


def main(arg):
    print(arg)

main(sys.argv[1])
